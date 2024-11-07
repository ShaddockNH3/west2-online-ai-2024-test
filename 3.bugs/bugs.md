### 学习目标：

- 爬虫初步学习
    - 网页抓包工具的使用
    - 网络请求的处理（requests库的使用）
    - 数据的提取（xpath(推荐)、bs4、···）
    - selenium的使用

那么开始。

由于b战视频那个项目寄了，所以这次后面换python3网络实战的那个

### 基本信息

robots.txt协议
君子协议，规定了网站中哪些数据可以被爬虫爬取

常用请求头信息
-User-Agent: 请求身份表示
-Connection:请求完毕后，是断开连接还是保持连接

常用响应头信息：
-Content-Type:服务器相应会客户端的数据类型

Https协议：
-安全的超文本传输协议

加密方式
-对称密钥加密：客户端发送过来密钥和密文，服务器端解密就得到了数据
-非对称密钥加密：让服务器端去设定加密方式（公钥），发送给客户端，然后客户端将该密文发给服务器端，然后服务器端用（密钥）自己解开
安全隐患：
无法保证服务器端收到正确公钥

-证书密钥加密：证书认证机构，服务器端和客户端比较信任
服务器端把公钥给证书认证机构审核，证书认证机构进行数字签名，然后封装到证书中，最后发送给客户端
### request

先复习一下基本的东西

爬取网页分三步走，第一步制定url，第二部发送请求，第三步获取数据txt，最后持久化存储数据。

requests模块：基于网络请求的的模块

作用：模拟浏览器法请求

如何使用（requests模块的编码流程）

- 指定url（输入具体网址）
- 发起请求
- 获取响应数据
- 持久化存储

以最简单的爬取搜狗网站为例，代码如下：

```
import requests  

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
    with open('./1.0 sogou.html','w',encoding='utf-8') as fp:  
        fp.write(page_text)  
    print("爬取结束")
```

由于门户网站会检测对应的载体身份标识，如果检测到的是一个正常的请求，那么通过。如果检测到了不正常的请求，比如说爬虫，服务器可能会拒绝该请求。

正常地标识是通过浏览器进入，而异常的标识则不是通过浏览器进入。

为了对应这一点，所以我们需要进行UA伪装。

![[P1.png]]

通过如上的界面，成功找到UA

此时先使用一个字典，封装入我们的headers，即

```
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
```

然后我们爬虫需要用的是什么？需要动态的。所以此时引入一个param。

代码如下：

```
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
```

上述的代码尚且还有一点点小小的不合适的地方，不需要看，现在主要就是看下面的东西。

上面代码怪怪的。

翻到百度翻译

![[P2.png]]

这里是post请求，所以也得更改成post，然后这里返回的类型是json，所以得用json接受

![[Pasted image 20241103221752.png]]

翻到payload界面，可以看到这里的data需要传入kw

所以代码如下：

```
import requests  
import json  
  
if __name__=="__main__":  
  
    headers={  
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'  
    }  
  
    url = 'https://fanyi.baidu.com/sug'  
    word=input("enter a word:")  
    data={  
        'kw':word  
    }  
  
    response=requests.post(url=url,data=data,headers=headers)  
  
    dic_obj=response.json()  
  
    print(dic_obj)  
  
    fileName='1.2 '+word+'.json'  
  
    fp=open(fileName,'w',encoding='utf-8')  
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
```

输入及输出：

```
enter a word:cat
{'errno': 0, 'data': [{'k': 'cat', 'v': 'n. 猫; 猫科动物; 狠毒的女人; 爵士乐爱好者 vt. 把（锚）吊放在锚架上; 〈俚〉寻欢，宿娼'}, {'k': 'CAT', 'v': 'abbr. Carburetor Air Temperature 汽化器空气温度'}, {'k': 'Cat', 'v': '[人名] 卡特'}, {'k': 'CaT', 'v': 'abbr. calcium tartrate tetrahydrate 酒石酸钙四水合物'}, {'k': 'cata', 'v': '[机] 渺位; 依照'}], 'logid': 1166652942}
```

解释一下代码。

`json.dump`代码的意思是说，将dic_obj以json格式写入fp文件中，后面的`ensure_ascii=False`，意思是说，本来默认也是对中文使用ascii码，现在要取消

那么就破解了百度翻译。

其实这里还是有点没懂，不过无所谓了，今天先到这里。
