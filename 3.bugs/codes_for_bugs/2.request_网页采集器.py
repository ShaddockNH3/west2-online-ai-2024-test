'''
UA检测，门户网站会检测对应的载体身份标识
如果检测到请求的是一个正常请求
不正常请求（爬虫）服务器有可能会拒绝该请求。
正常标识是浏览器，不是正常标识的话不是浏览器
'''

'''
UA伪装，让爬虫对应身份表示伪装成某个浏览器
'''


import requests
if __name__=="__main__":
    #UA伪装
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    url='https://sogou.com/web'
    #需要设置成动态的：封装到字典中
    word=input('enter a word:')
    param={
        'query':word
    }
    #对指定的url发起的请求对应的url是携带参数的
    response=requests.get(url=url,params=param,headers=headers)

    page_text=response.text
    fileName=word+'.html'

    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,"OK")
