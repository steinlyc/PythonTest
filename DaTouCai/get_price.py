import requests
import datetime
from twilio.rest import Client
from threading import Timer


def GetData():
    res = requests.get('http://ttc.21hz.top/turniptrade/island/list/1')
    res = res.json()
    res = res['list']
    return res


def Sorted_list():
    sorted_list = sorted(GetData(), key=lambda x: x['price'], reverse=True)
    return sorted_list


def GetPrice(t):
    for item in Sorted_list():
        if item['price'] > 500:
            Send(item['price'])
            t.cancel()
            print('找到目标价格:' + str(item['price']))
            return
        else:
            pass
    print('查询中...' + GetLocalTime())


def GetLocalTime():
    local_time = datetime.datetime.now()
    local_time = datetime.datetime.strftime(local_time, '%Y-%m-%d %H:%M:%S')
    return str(local_time)


def Send(price):
    account_sid = "AC865ccf94cb13b997a3634654275ff8b2"
    auth_token = "c06ecf26977476f968eff1218eec33ab"
    client = Client(account_sid, auth_token)
    message = client.messages.create(to="+8615365108233",
                                     from_="+18125419480",
                                     body='找到大头菜目标价格:' + str(price))
    print(message.sid)


def PrinTime(time):
    global t
    t = Timer(time, PrinTime, (time, ))
    GetPrice(t)
    t.start()


PrinTime(30)