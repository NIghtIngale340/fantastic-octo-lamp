import hashlib, hmac, yaml
cfg = yaml.safe_load(open('/home/nightingale/CTF/PCGCTF/unsolved/reconnaissance/122-pcgctf-juice-shop-gateway/files/docker-compose.yml'))
key = cfg['services']['juice-shop']['environment']['CTF_KEY']
print(hmac.new(key.encode(), b'Score Board', hashlib.sha1).hexdigest())
