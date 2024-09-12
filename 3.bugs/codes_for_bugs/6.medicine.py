import requests

if __name__=='__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    url='https://bt.gsxt.gov.cn/corp-query-entprise-info-hot-search-list.html?province=440000'
    response=requests.get(url=url,headers=headers)

    page_text=response.text

    with open('en.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("OK!!")

    #直接获取网页是获取不了超链接里的内容的！
    #动态数据


