'''''
3.爬取豆瓣首页的图片
'''

import urllib.request, socket, re, sys, os

targetPath = "imgs"


def saveFile(path):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos + 1:])
    return t


# 地址
url = "http://www.douban.com"

header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

# 请求
request = urllib.request.Request(url, headers=header)

# 爬取结果
response = urllib.request.urlopen(request)

data = response.read()

for link, t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link, saveFile(link))
    except:
        print('fail')
