'''''
2.爬取豆瓣首页, 并保存
'''

import urllib.request

# 保存文件
def saveFile(data):
  path = "files/douban.html"
  f = open(path, 'wb')
  f.write(data)
  f.close()

headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

# 地址
url = "http://www.douban.com"

# 请求
request = urllib.request.Request(url, headers=headers)

# 爬取结果
response = urllib.request.urlopen(request)

data = response.read()

# 解码方式
decodeData = data.decode('utf-8')

saveFile(data)

