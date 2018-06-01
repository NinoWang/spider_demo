'''''
1.爬取豆瓣首页 
'''

import urllib.request

# 地址
url = "http://www.douban.com"

header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

# 请求
request = urllib.request.Request(url, headers=header)

# 爬取结果
response = urllib.request.urlopen(request)

# 解码方式
data = response.read().decode('utf-8')

# print(data)

print('response ↓↓↓↓↓↓\n', type(response), '\n')

print('url ↓↓↓↓↓↓\n', response.geturl(), '\n')

print('info ↓↓↓↓↓↓\n', response.info(), '\n')

print('code ↓↓↓↓↓↓\n', response.getcode(), '\n')

