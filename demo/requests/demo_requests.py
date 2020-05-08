import requests
import json

url = 'http://api.fowallet.net/1.0/app'
data = '''{
            count_deal(
                where:{
                    fromaccount_id:{
                        ne: "buyoutworker"
            },
            toaccount_id:{
                ne: "buyoutworker"
            }
            tokenpair_id:{
                eq: "1"
            }  
            },
            order: "-created"
        )
    }'''
headers = {'Content-Type': 'application/graphql'}

res = requests.post(url=url, data=data, headers=headers).json()

# loads是把字符串转化成字典，dumps是把字典转化成字符串
# 还有load和dump 这是对文件处理，load从文件里读取不需要read()loads需要，dump写入文件不需要write()而dumps需要
# strjson = json.loads(res)
# jsondata = json.dumps(strjson)
# print(type(strjson))
# print(type(jsondata))

# 格式化需要调用json库 indent 缩进
res = json.dumps(res, indent=2, ensure_ascii=False)
print(res)