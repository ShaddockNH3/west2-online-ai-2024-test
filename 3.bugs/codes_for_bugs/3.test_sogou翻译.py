import requests
import json

if __name__=='__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    #指定url
    post_url='https://fanyi.sogou.com/reventondc/suggV3'

    #post请求参数处理
    word=input("enter a word:")
    data={
        'from': 'auto',
        'to': 'zh-CHS',
        'client':'web',
        'text': word,
        'uuid': '4a4b2e21-9b63-46c1-a234-1e1cb6901b7f',
        'pid': 'sogou-dict-vr',
        'addSugg': 'on',
    }


    response=requests.post(url=post_url,data=data,headers=headers)

    dic_obj=response.json()#返回的是字典对象

    print(dic_obj)
    fileName=word+".json"
    fp=open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over!!!')
