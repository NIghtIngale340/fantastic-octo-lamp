import sys,subprocess,time
from pathlib import Path
R=Path('/home/nightingale/CTF/PCGCTF');W=Path(__file__).resolve().parent;i=int(sys.argv[1]);stamp=str(time.time_ns())
if i==1:
 h=W/'001.sha1';h.write_text('530d378bd60243f41d169aad7cd238ae816a6ee3\n');args=['john','--format=Raw-SHA1','--wordlist=/usr/share/wordlists/rockyou.txt','--max-run-time=20','--pot='+str(W/'001-capture.pot'),'--session='+str(W/('001-'+stamp)),str(h)]
else:
 archive=R/'solved/steganography/071-embedded-text/files/embedded-text.zip';r=subprocess.run(['zip2john',str(archive)],capture_output=True,text=True,check=True);h=W/'071.hash';h.write_text(r.stdout);print(r.stderr.strip());args=['john','--wordlist=/usr/share/wordlists/rockyou.txt','--max-run-time=20','--pot='+str(W/'071-capture.pot'),'--session='+str(W/('071-'+stamp)),str(h)]
import shlex
print('Executing:',shlex.join(args),flush=True);p=subprocess.run(args);print('John process exit:',p.returncode);print('Bound: at most20seconds; actual run output determines whether dictionary completed. No success is invented.')
