import requests
from twilio.rest import Client
import json
import datetime
import time
import timedelta
from threading import Timer
import pprint
account_sid = "AC857d00f68fe0bc00164e5e2477fb145f"
auth_token = "dbf8a58e4eef7b22f8d8070ca663fee5"
url = "http://api.fowallet.net/1.0/app/blocks"
data = {'order': '-id'}
res = requests.get(url, params=data)
res_json = res.json()

# 获取utc时间
utc_time = res_json[0]['block_time']
utcstring = "%Y-%m-%dT%H:%M:%S.%fZ"
utc_format = datetime.datetime.strptime(utc_time, utcstring)
utc_format_8 = utc_format + datetime.timedelta(hours=8)

# 获取本地时间
local_time = datetime.datetime.now()
local_formatstrftime = datetime.datetime.strftime(local_time,
                                                  '%Y-%m-%d %H:%M:%S')
local_formatstrptime = datetime.datetime.strptime(local_formatstrftime,
                                                  '%Y-%m-%d %H:%M:%S')
Time_diff = str(abs(local_formatstrptime - utc_format_8))


#将时间差转换成秒数
def Conver(Time_diff):
    h, m, s = Time_diff.strip().split(":")
    Sum_time = int(h) * 3600 + int(m) * 60 + int(s)
    return Sum_time


Con_time = Conver(Time_diff)


# # 打印时间函数
def printTime(time):
    t = Timer(time, printTime, (time, ))
    localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def Send():
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+8615266905059",
            from_="+17326622713",
            body="同步数据节点异常!,本地时间与服务器时间差为：{}秒".format(Con_time))
        print(message.sid)
        print("本地时间为：{}".format(localtime))
        print("服务器时间为:{}".format(utc_time))
        print("本地时间与服务器时间差为：{}秒".format(Con_time))
        print("节点异常")

    if Con_time <= 3600:
        print('程序正在运行')
        print(localtime)
    elif Con_time > 3600:
        Send()
        t.cancel()
    t.start()


printTime(3600)
