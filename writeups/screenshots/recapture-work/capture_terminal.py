import os, subprocess, time, shlex, json, hashlib
from pathlib import Path
root=Path('/home/nightingale/CTF/PCGCTF/final-writeups')
work=root/'screenshots/recapture-work'; work.mkdir(exist_ok=True)
job={'id':34,'cwd':str(work),'commands':["printf '%s\\n' 'synt vf pbby' | tr 'A-Za-z' 'N-ZA-Mn-za-m'"],'name':'034-simple-rot13'}
jobfile=work/'pilot.json'; jobfile.write_text(json.dumps([job]))

def capture(job):
 name=job['name']; folder=work/name; folder.mkdir(exist_ok=True)
 done=folder/'done'; done.unlink(missing_ok=True)
 log=folder/'output.log'; script=folder/'run.sh'; title='ctf-recapture-'+name
 lines=['#!/bin/bash',f'cd {shlex.quote(job["cwd"])} || exit 1',f'exec > >(tee {shlex.quote(str(log))}) 2>&1',"printf '\\033[2J\\033[H'"]
 for cmd in job['commands']:
  lines += ["printf '%s\\n' "+shlex.quote('$ '+cmd),cmd,'result=$?',f'printf "%s\\n" "$result" >> {shlex.quote(str(folder/"exit-codes"))}',"printf '\\n'"]
 lines += [f'touch {shlex.quote(str(done))}',"printf '$ '", 'sleep 120']
 script.write_text('\n'.join(lines)+'\n')
 env=dict(os.environ,DISPLAY=':100',QT_QPA_PLATFORM='xcb',XDG_RUNTIME_DIR='/tmp/opencode/run')
 proc=subprocess.Popen(['konsole','--separate','--hide-menubar','--hide-tabbar','-p','Font=JetBrains Mono,13','-p','ColorScheme=Breeze','-p','TerminalColumns=112','-p',f'TerminalRows={job.get("rows",14)}','-p','ScrollBarPosition=0','-p','TerminalMargin=12','-p','tabtitle='+title,'--hold','-e','bash',str(script)],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 try:
  deadline=time.time()+80;wid=None
  while time.time()<deadline:
   if proc.poll() is not None: raise RuntimeError(proc.stderr.read().decode())
   tree=subprocess.check_output(['xwininfo','-root','-tree'],env=env,text=True)
   for line in tree.splitlines():
    if title in line:
     import re
     match=re.search(r'0x[0-9a-f]+',line)
     if match:wid=match[0]
   if wid and done.exists():break
   time.sleep(.15)
  if not wid or not done.exists():raise RuntimeError('Capture timed out: '+name)
  time.sleep(.4)
  out=root/'screenshots'/f'{name}.png'
  subprocess.run(['import','-window',wid,str(out)],env=env,check=True)
  assert out.stat().st_size>2000
  return {**job,'image':'screenshots/'+out.name,'log':str(log),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'exit_codes':(folder/'exit-codes').read_text().splitlines(),'method':'Commands freshly executed inside the captured Konsole window; not a transcript replay','captured_at':time.strftime('%Y-%m-%dT%H:%M:%S%z')}
 finally:
  proc.terminate()
  try:proc.wait(timeout=3)
  except subprocess.TimeoutExpired:proc.kill()
if __name__=='__main__':
 import sys
 jobs=json.loads(Path(sys.argv[1] if len(sys.argv)>1 else jobfile).read_text()); results=[]
 target=work/'fresh-captures.json'
 if target.exists():results=json.loads(target.read_text())
 for job in jobs:
  if any(r['name']==job['name'] for r in results):continue
  try:
   result=capture(job);results.append(result);target.write_text(json.dumps(results,indent=2)+'\n');print(job['name'],result['exit_codes'],flush=True)
  except Exception as e:print('FAILED',job['name'],str(e),flush=True)
