import requests

if __name__=="__main__":

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    url = 'https://www.google.com/search?'
    kw=input("enter a word:")
    param={
        'q':kw
    }

    response=requests.get(url=url,params=param,headers=headers)

    page_text=response.text

    print(page_text)

    fileName=kw+'.html'

    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("OK")