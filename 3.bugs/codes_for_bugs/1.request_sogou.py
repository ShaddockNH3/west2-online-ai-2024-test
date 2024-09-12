import requests
#指定url
if __name__ == "__main__":
    #指定url
    url='http://www.sogou.com/'
    #第二步，发送请求
    #返回响应对象
    response=requests.get(url=url)
    #第三步，获取响应数据(txt)
    page_text=response.text
    print(page_text)
    #持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取结束")
