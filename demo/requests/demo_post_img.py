import requests
import json

url = 'https://www.imooc.com/user/postpic'
file = {
    'fileField': ('logo.png',
                  open('/Users/stein/Documents/DexTools/src/statics/logo.png',
                       'rb'), 'image/png'),
    'type':
    '1'
}
cookies = {
    'apsid':
    'Q2YTI3YWZkMjU4ZDNhMjA0ZjgzZWM2MzBlNWQ1MjQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjk3MTA1OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzMzEwOTc1NDNAcXEuY29tAAAAAAAAAAAAAAAAAAAAADVkMDZmZTdiYTAyYWU1MTYwYTdjNjNjODA0YTg0MTU2STWtXkk1rV4%3DMW'
}

# verify=False https的验证警告关闭
res = requests.post(url=url, files=file, cookies=cookies, verify=False).json()
print(res)