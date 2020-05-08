import requests
import json

url = 'http://file.mukewang.com/apk/app/117/imooc7.3.610102001android.apk?version=1588585458'

cookies = {
    'apsid':
    'Q2YTI3YWZkMjU4ZDNhMjA0ZjgzZWM2MzBlNWQ1MjQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjk3MTA1OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzMzEwOTc1NDNAcXEuY29tAAAAAAAAAAAAAAAAAAAAADVkMDZmZTdiYTAyYWU1MTYwYTdjNjNjODA0YTg0MTU2STWtXkk1rV4%3DMW'
}

res = requests.get(url=url)

# 下载文件，需要把下载文件的content写入到文件当中
with open('test.apk','wb') as f:
    f.write(res.content)
print(res)