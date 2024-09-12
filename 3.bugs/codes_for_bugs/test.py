import requests


if __name__=='__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    #按照城市查询
    post_url='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'
    param={
        'op': 'cname',
        'cname': '福州',
        'pid': '',
        'pageIndex': '1',
        'pageSize': '10'
    }

    response=requests.post(url=post_url,params=param,headers=headers)

    page_text=response.text
    with open('kfc.txt','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("OK!")
    