from urllib import request
import ssl
import re

# 当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出错误消息,需在全局添加如下代码
ssl._create_default_https_context = ssl._create_unverified_context


class Spier(object):
    url = 'https://www.huya.com/g/wzry'
    root_node = r'<span class="avatar fl">([\s\S]*?)<span class="num">([\s\S]*?)</span>'
    name_node = r'<i class="nick" title="([\s\S]*?)">'
    num_node = r'<i class="js-num">([\s\S]*?)</i>'

    def __contect(self):
        res = request.urlopen(Spier.url)
        htmls = res.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        node_list = re.findall(Spier.root_node, htmls)
        anchors = []
        for node in node_list:
            name = re.findall(Spier.name_node, str(node))
            num = re.findall(Spier.num_node, str(node))
            anchor = {'name': name, 'num': num}
            anchors.append(anchor)
        return anchors

    # 数据精炼，已在analysis内部完成，故注释
    def __refine(self, anchors):
        func = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'num': anchor['num'][0]
        }
        return map(func, anchors)

    def __sortfix(self, anchors):
        anchors = sorted(anchors, key=self.__sortfunc, reverse=True)
        return anchors

    def __sortfunc(self, anchors):
        res = re.findall(r'([\s\S]*?)[万人]', anchors['num'])
        num = float(res[0])
        if '万' in anchors['num']:
            num *= 10000
        return num

    def __show(self, anchors):
        for item in range(0, len(anchors)):
            print('No.' + str(item + 1) + ' ' + anchors[item]['name'] +
                  '------' + anchors[item]['num'])

    def go(self):
        htmls = self.__contect()
        anchors = self.__analysis(htmls)
        res = list(self.__refine(anchors))
        res = self.__sortfix(res)
        self.__show(res)


spier = Spier()
spier.go()