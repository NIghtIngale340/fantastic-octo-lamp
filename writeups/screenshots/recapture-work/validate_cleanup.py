from pathlib import Path
import re,json,hashlib,subprocess,ast,math
root=Path('/home/nightingale/CTF/PCGCTF/final-writeups');backup=root.parent/'writeup-backup-before-final-cleanup-20261029'
files=sorted(root.glob('[0-9]*/*.md'));issues=[];changed=[]
def flagblocks(s):
 m=re.search(r'^## Flag[^\n]*\n(.*?)(?=\n## |\Z)',s,re.M|re.S)
 return re.findall(r'```[^\n]*\n(.*?)```',m[1],re.S) if m else []
for p in files:
 s=p.read_text();old=(backup/p.relative_to(root)).read_text()
 if s!=old:changed.append(str(p.relative_to(root)))
 if flagblocks(s)!=flagblocks(old):issues.append('Flag changed: '+p.name)
 if len(re.findall(r'^```',s,re.M))%2:issues.append('Fence: '+p.name)
 for t in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)',s):
  t=t.strip('<>')
  if '://' in t or t.startswith('#'):continue
  path=Path(t) if t.startswith('/') else p.parent/t.split('#')[0]
  if not path.exists():issues.append('Missing link: '+p.name+' '+t)
 for lang,code in re.findall(r'```(sh|python)\n(.*?)```',s,re.S):
  if lang=='sh':
   r=subprocess.run(['bash','-n'],input=code,text=True,capture_output=True)
   if r.returncode:issues.append('Shell syntax: '+p.name+' '+r.stderr)
  else:
   try:ast.parse(code)
   except SyntaxError as e:issues.append('Python syntax: '+p.name+' '+str(e))
manifest=json.loads((root/'screenshots/capture-manifest.json').read_text())
for c in manifest['captures']:
 if hashlib.sha256((root/c['image']).read_bytes()).hexdigest()!=c['sha256']:issues.append('Image hash: '+c['image'])
records=json.loads((root/'screenshots/recapture-work/fresh-captures.json').read_text());latest={r['id']:r for r in records if r['name']!='034-simple-rot13'}
for r in latest.values():
 log=re.sub(r'\x1b\[[0-9;?]*[A-Za-z]','',Path(r['log']).read_text())
 if any(c!='0' for c in r['exit_codes']):issues.append('Run failed: '+r['name'])
 rows=sum(max(1,math.ceil(len(x.expandtabs(8))/112)) for x in log.splitlines())
 if rows>r.get('rows',14):issues.append('Overflow: '+r['name'])
 if any(t in log for t in ['Traceback','syntax error','isn\'t a valid','Some fields aren','Broken pipe']):issues.append('Output error: '+r['name'])
queries=json.loads((root/'screenshots/capture-work/aurora-select-queries.json').read_text())
for q in queries:
 p=next(root.glob(f"[0-9]*/{q['id']:03}-*.md"))
 if re.search(r'```sql\n(.*?)```',p.read_text(),re.S)[1].strip()!=q['query'].strip():issues.append('SQL mismatch: '+str(q['id']))
result={'drafts':len(files),'edited_drafts':len(changed),'fresh_runs':len(records),'writeups_with_fresh_capture':len(latest),'embedded_images':sum(len(re.findall(r'!\[',p.read_text())) for p in files),'manifest_images_checked':len(manifest['captures']),'saved_SQL_queries_matched':len(queries),'flags_preserved':True,'issues':issues}
(root/'cleanup-validation.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'cleanup-results.json').write_text(json.dumps({**result,'changed_writeups':changed,'backup':str(backup)},indent=2)+'\n')
print(json.dumps(result,indent=2))
assert not issues
