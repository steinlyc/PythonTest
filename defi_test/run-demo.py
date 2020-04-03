import requests
import json
from config import config


class find_key_words():
      
  url = config['url']
  headers = config['headers']
  params = config['params']
  key_words = config['key']

  def find_article(self):
    res = requests.post(find_key_words.url, data=find_key_words.params, headers=find_key_words.headers)
    res = res.json()
    res = res['data']['find_article']
    return res

  def refine_article(self,res):
    article_list = []
    for item in res:
      article_list.append({'title': item['title'],'content': item['content'],'id':item['id']})
    return article_list

  def check_kw(self,article_list):
    check_list = article_list
    for key in find_key_words.key_words:
      temp_list = []
      for item in check_list:
        if (key in item['title'] or key in item['content']):
          pass
        else:
          temp_list.append(item)
      check_list = temp_list
    return check_list

  def duplicate(self,data):
    check_list = []
    for item in data:
      if item not in check_list:
        check_list.append(item)
    return check_list
  
  def show(self,data):
    for item in data:
      print('文章id: '+str(item['id'])+'--------'+'标题: '+item['title'])
    

  def go(self):
    res = self.find_article()
    article_list = self.refine_article(res)
    print('文章总数: '+str(len(article_list)))
    check_list = self.check_kw(article_list)
    check_list = self.duplicate(check_list)
    print('共筛选出: '+str(len(check_list)))
    self.show(check_list)

check = find_key_words()
check.go()