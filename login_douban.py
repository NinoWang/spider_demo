import requests
import urllib
import re
import getpass
from bs4 import BeautifulSoup
from PIL import Image

# header
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

url = 'https://accounts.douban.com/login'
group_url = "https://www.douban.com/group/"
following_url = "https://www.douban.com/contacts/list"
followed_url = "https://www.douban.com/contacts/rlist"

session = requests.Session()
session.headers.update(headers)


# 登录
def login(username,
          password,
          source='index_nav',
          redir='https://www.douban.com/',
          login='登录'):
    caprcha_id, caprcha_link = get_captcha(url)  #获取get_captcha函数返回的值
    #如果有caprcha_id, 保存验证码图片并打开
    if caprcha_id:
        img_html = session.get(caprcha_link)
        with open('caprcha.jpg', 'wb') as f:
            f.write(img_html.content)
        try:
            im = Image.open('caprcha.jpg')
            im.show()
            im.close()
        except:
            print('打开错误')
        caprcha = input('请输入验证码：')
    data = {
        'source': source,
        'redir': redir,
        'form_email': username,
        'form_password': password,
        'login': login,
    }
    #如果需要验证码，将下面字段加入请求参数
    if caprcha_id:
        data['captcha-id'] = caprcha_id
        data['captcha-solution'] = caprcha
    html = session.post(url, data=data, headers=headers)
    return html


#解析登入界面，获取caprcha_id和caprcha_link
def get_captcha(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    caprcha_link = soup.select('#captcha_image')[0]['src']
    #lzform > div.item.item-captcha > div > div > input[type="hidden"]:nth-child(3)
    caprcha_id = soup.select('div.captcha_block > input')[1]['value']
    return caprcha_id, caprcha_link


# 爬取标题
def find_acticle_title(res):
    page = res.text
    soup = BeautifulSoup(page, "html.parser")
    result = soup.findAll('div', attrs={'class': 'title'})
    for item in result:
        print(item.find('a').get_text())


# 爬取小组话题
def find_group_subject():
    group_html = session.get(group_url)
    soup = BeautifulSoup(group_html.text, 'lxml')
    titles = soup.select('tr.pl > td.td-subject > a.title')
    for title in titles:
        print(title['href'], title.string)


# 爬取关注的人
def find_following():
  following_html = session.get(following_url)
  soup = BeautifulSoup(following_html.text, 'lxml')
  faces = soup.select('li.clearfix > a > img.face')
  for name in faces:
    print(name['alt'], name['src'])

# 爬取粉丝
def find_followed():
  followed_html = session.get(followed_url)
  soup = BeautifulSoup(followed_html.text, 'lxml')
  faces = soup.select('li.clearfix > a > img.face')
  for name in faces:
    print(name['alt'], name['src'])


print("欢迎登录豆瓣！")
email = input('请输入邮箱：')
password = getpass.getpass(prompt="请输入密码：")

# 发起登录请求
res = login(email, password)
while True:
    print('\n选取你要爬取的内容： 1.热门精选的标题  2.小组话题动态  3.关注的人  4.粉丝  0.退出')
    index = input('输入你的选项：')
    if index == '1':
        find_acticle_title(res)
    elif index == '2':
        find_group_subject()
    elif index == '3':
        find_following()
    elif index == '4':
        find_followed()
    else:
        exit()
    if index == 0:
        break
