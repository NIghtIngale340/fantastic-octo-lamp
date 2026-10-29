"""Reproduce the documented reversible CTF simulator actions; do not expose session tokens."""
import requests,json,sys,re
B='http://emedra.dctf.io:8080';i=int(sys.argv[1]);s=requests.Session()
def clean(v):
 if isinstance(v,dict):return {k:('[REDACTED_SESSION_TOKEN]' if 'token' in k.lower() and not (isinstance(x,str) and x.startswith('deadface{')) else clean(x)) for k,x in v.items()}
 if isinstance(v,list):return [clean(x) for x in v]
 return v
def post(path,obj):
 r=s.post(B+path,json=obj,timeout=15);r.raise_for_status();return r.json()
def show(obj):print(json.dumps(clean(obj),indent=2))
if i==315:
 r=s.get(B+'/api/kiosk/login',timeout=15);print('GET /api/kiosk/login — HTTP',r.status_code)
 for line in r.text.splitlines():
  if 'TODO' in line or 'deadface{' in line:print(line.strip())
elif i==316:
 r=post('/api/kiosk/auth',{'username':'emedra-svc','password':'ChangeMe!2019'});print('POST /api/kiosk/auth — documented factory training credentials');show(r)
elif i==317:
 c=post('/api/connect',{'tool':'hdmi','port':'hdmi'});print('Connected HDMI training tool:');show(c)
 r=s.get(B+'/api/external-display',params={'level':3},headers={'Authorization':'Bearer '+c['token']},timeout=15);print('GET /api/external-display?level=3 — HTTP',r.status_code);show(r.json())
elif i==318:
 a=post('/api/kiosk/auth',{'username':'emedra-svc','password':'ChangeMe!2019'});c=post('/api/connect',{'tool':'live-linux','port':'usb-a'});print('Authenticated and connected the Live Linux training tool.');show(c)
 for line in ['cat README.txt','sudo mount /dev/sda2 /mnt','cat /mnt/opt/scanworks/config.yaml']:
  print('\nSimulator shell command:',line);r=post('/api/shell',{'token':c['token'],'line':line});show(r)
