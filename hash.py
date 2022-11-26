import hashlib


mail = "abc@gmail.com"
pwd = "password"

pwd_encode = pwd.encode()

pwd_hash = hashlib.md5(pwd_encode).hexdigest()

print(pwd)
print(pwd_encode)
# print(pwd_encode)
print(pwd_hash)