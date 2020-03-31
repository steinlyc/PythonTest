from urllib import request
import ssl

# 当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出错误消息,需在全局添加如下代码
ssl._create_default_https_context = ssl._create_unverified_context


class Spier(object):
    url = 'https://www.huya.com/g/wzry'

    def __contect(self):
        res = request.urlopen(Spier.url)
        htmls = res.read()
        return htmls

    def __analysis(self, htmls):
        print(htmls)

    def go(self):
        htmls = self.__contect()
        self.__analysis(htmls)


spier = Spier()
spier.go()