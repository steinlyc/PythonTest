import hashlib

# name = 'liyuchen123'
# hash = hashlib.sha256()
# hash.update(name.encode('utf-8'))
# res = hash.hexdigest()
# print(res)


# name = 'liyuchen'
# name2 = '123'
# hash = hashlib.sha256()
# hash.update(name.encode('utf-8'))
# hash.update(name2.encode('utf-8'))
# res = hash.hexdigest()
# print(res)


name = 'liyuchen'
name2 = '123'
hash = hashlib.sha256()
hash.update(name.encode('utf-8'))
res = hash.hexdigest()
print(res)
hash.update(name2.encode('utf-8'))
res = hash.hexdigest()
print(res)