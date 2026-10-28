import asyncio,base64,json,os,pty,select,shlex,signal,struct,subprocess,time,fcntl,termios
from pathlib import Path
from aiohttp import web
WORK=Path(__file__).resolve().parent;ROOT=Path('/home/nightingale/CTF');OUT=WORK.parent
HTML='''<!doctype html><meta charset="utf-8"><title>PCGCTF — Actual terminal capture</title><link rel="stylesheet" href="/vendor/xterm.css"><style>body{margin:0;background:#0c121a;color:#e6edf3;font:14px system-ui}header{padding:12px 20px;border-bottom:1px solid #344050;display:flex;justify-content:space-between}h1{font-size:16px;margin:0}#terminal{padding:14px}button{color:inherit;background:#223044;border:1px solid #556277;padding:4px 12px}#status{font-weight:600}</style><header><div><h1 id="title">PCGCTF — actual local terminal session</h1><span>Real PTY output • no simulated results</span></div><div><button onclick="term.scrollToTop()">Top</button> <button onclick="term.scrollToBottom()">Latest output</button> <span id="status">Running</span></div></header><div id="terminal"></div><script src="/vendor/xterm.js"></script><script>const term=new Terminal({cols:140,rows:34,fontSize:14,fontFamily:'DejaVu Sans Mono,monospace',theme:{background:'#0c121a',foreground:'#e6edf3'},scrollback:5000,disableStdin:true,convertEol:false});term.open(document.getElementById('terminal'));const job=new URLSearchParams(location.search).get('job');document.getElementById('title').textContent='PCGCTF — '+job;const events=new EventSource('/events/'+encodeURIComponent(job));events.onmessage=e=>{const m=JSON.parse(e.data);if(m.data){const bytes=Uint8Array.from(atob(m.data),x=>x.charCodeAt(0));term.write(bytes);}if(m.done){term.write('\\r\\n',()=>{document.getElementById('status').textContent='Process finished';events.close();term.scrollToBottom();});}};</script>'''
async def page(request):return web.Response(text=HTML,content_type='text/html')
async def vendor(request):
 name=request.match_info['name']
 if name not in ['xterm.js','xterm.css']:raise web.HTTPNotFound()
 return web.FileResponse(WORK/'vendor'/name)
async def events(request):
 jobid=request.match_info['job'];jobs={j['key']:j for j in json.loads((WORK/'jobs.json').read_text())}
 if jobid not in jobs:raise web.HTTPNotFound()
 j=jobs[jobid];cmd=j['command'];started=time.time();master,slave=pty.openpty();fcntl.ioctl(slave,termios.TIOCSWINSZ,struct.pack('HHHH',34,140,0,0));env=dict(os.environ,TERM='xterm-256color',PYTHONUNBUFFERED='1',COLUMNS='140',LINES='34',NO_COLOR='1')
 script='printf "\\033[2J\\033[H"\nprintf "%s\\n" '+shlex.quote(j['title'])+'\nprintf "%s\\n\\n" '+shlex.quote('$ '+cmd)+'\ntimeout -k 2 90 bash --noprofile --norc -c '+shlex.quote(cmd)+'\nrc=$?\nprintf "\\n[Actual command exit code: %s]\\n" "$rc"\nexit "$rc"'
 proc=subprocess.Popen(['bash','--noprofile','--norc','-c',script],stdin=slave,stdout=slave,stderr=slave,cwd=str(ROOT),env=env,start_new_session=True);os.close(slave);os.set_blocking(master,False)
 response=web.StreamResponse(headers={'Content-Type':'text/event-stream','Cache-Control':'no-cache'});await response.prepare(request);raw=bytearray()
 try:
  while True:
   try:data=os.read(master,65536)
   except BlockingIOError:data=None
   except OSError:data=b''
   if data:
    raw.extend(data);await response.write(('data: '+json.dumps({'data':base64.b64encode(data).decode()})+'\n\n').encode())
   elif proc.poll() is not None:
    # Drain already-buffered final output before declaring completion.
    try:data=os.read(master,65536)
    except (OSError,BlockingIOError):data=b''
    if data:raw.extend(data);await response.write(('data: '+json.dumps({'data':base64.b64encode(data).decode()})+'\n\n').encode())
    break
   await asyncio.sleep(.03)
  code=proc.wait();(WORK/(jobid+'.terminal.log')).write_bytes(raw);record={**j,'exit_code':code,'started_at_unix':started,'finished_at_unix':time.time(),'log':str(WORK/(jobid+'.terminal.log')),'capture_type':'Actual local PTY session, rendered by xterm.js'};(WORK/(jobid+'.result.json')).write_text(json.dumps(record,indent=2)+'\n');await response.write(('data: '+json.dumps({'done':True,'exit_code':code})+'\n\n').encode());await response.write_eof()
 finally:
  os.close(master)
  if proc.poll() is None:
   try:os.killpg(proc.pid,signal.SIGTERM)
   except ProcessLookupError:pass
 return response
async def artifact(request):
 mapping=json.loads((WORK/'artifacts.json').read_text());key=request.match_info['key']
 if key not in mapping:raise web.HTTPNotFound()
 return web.FileResponse(mapping[key])
app=web.Application();app.router.add_get('/',page);app.router.add_get('/vendor/{name}',vendor);app.router.add_get('/events/{job}',events);app.router.add_get('/artifact/{key}',artifact)
web.run_app(app,host='127.0.0.1',port=8769,print=None)
