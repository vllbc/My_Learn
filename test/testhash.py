import hashlib

text = '1122131231'

print(hashlib.md5(text.encode()).hexdigest())