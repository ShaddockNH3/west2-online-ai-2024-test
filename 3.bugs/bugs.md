### 学习目标：

- 爬虫初步学习
    - 网页抓包工具的使用
    - 网络请求的处理（requests库的使用）
    - 数据的提取（xpath(推荐)、bs4、···）
    - selenium的使用

那么开始。

### re正则表达式

#### 1.匹配规则

先贴一个匹配规则在这里

| 模　　式     | 描　　述                                              |
| -------- | ------------------------------------------------- |
| `\w`     | 匹配字母、数字及下划线                                       |
| `\W`     | 匹配不是字母、数字及下划线的字符                                  |
| `\s`     | 匹配任意空白字符，等价于 `[\t\n\r\f]`                         |
| `\S`     | 匹配任意非空字符                                          |
| `\d`     | 匹配任意数字，等价于 `[0-9]`                                |
| `\D`     | 匹配任意非数字的字符                                        |
| `\A`     | 匹配字符串开头                                           |
| `\Z`     | 匹配字符串结尾，如果存在换行，只匹配到换行前的结束字符串                      |
| `\z`     | 匹配字符串结尾，如果存在换行，同时还会匹配换行符                          |
| `\G`     | 匹配最后匹配完成的位置                                       |
| `\n`     | 匹配一个换行符                                           |
| `\t`     | 匹配一个制表符                                           |
| `^`      | 匹配一行字符串的开头                                        |
| `$`      | 匹配一行字符串的结尾                                        |
| `.`      | 匹配任意字符，除了换行符，当 `re.DOTALL` 标记被指定时，则可以匹配包括换行符的任意字符 |
| `[...]`  | 用来表示一组字符，单独列出，比如 `[amk]` 匹配 `a`、`m` 或 `k`         |
| `[^...]` | 不在 `[]` 中的字符，比如 匹配除了 `a`、`b`、`c` 之外的字符            |
| `*`      | 匹配 0 个或多个表达式                                      |
| `+`      | 匹配 1 个或多个表达式                                      |
| `?`      | 匹配 0 个或 1 个前面的正则表达式定义的片段，非贪婪方式                    |
| `{n}`    | 精确匹配 n 个前面的表达式                                    |
| `{n, m}` | 匹配 n 到 m 次由前面正则表达式定义的片段，贪婪方式                      |
| `ab`     | 匹配 a 或 b                                          |
| `()`     | 匹配括号内的表达式，也表示一个组                                  |

#### 2.match

常用的检测正则表达式是否匹配字符串，match会尝试从字符串起始位置匹配正则表达式的结果，如果不匹配，就会返回`None`

这里代码实现并不困难，只需要对照上面那张表即可

```
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())
```

那么这里的group和span是什么意思，span用于返回精确匹配的范围，而group则是可以通过索引进行访问正则表达式里的具体东西

==这里group没咋搞懂==

#### 提取部分，先跳（）

--
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

#### 基本的东西

代码：

```
import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text[:100])
print(r.cookies)
```

输出：

```
<class 'requests.models.Response'>
200
<class 'str'>
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charse
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
```

gpt：

1. import requests

导入 requests 库，这是 Python 中的一个用于处理 HTTP 请求的库。它提供了简单的方法来发送各种 HTTP 请求（如 GET、POST 等）并处理响应。

2. r = requests.get('https://www.baidu.com/')

调用 requests.get() 方法向 https://www.baidu.com/ 发送一个 GET 请求。

requests.get() 方法会发送一个 HTTP GET 请求，并返回一个 Response 对象，包含了响应的状态码、内容、头部信息和 cookies 等数据。

r 是返回的 Response 对象，后续的代码会通过这个对象来访问响应的各种信息。


3. print(type(r))

输出 r 的数据类型。

由于 requests.get() 返回的是一个 Response 对象，因此输出 <class 'requests.models.Response'>。

Response 对象封装了服务器返回的响应数据。


4. print(r.status_code)

输出 HTTP 响应的状态码。

status_code 是一个整数，表示服务器返回的 HTTP 状态码。常见状态码包括：

200 表示请求成功。

404 表示请求的页面未找到。

500 表示服务器内部错误。


如果百度的服务器正常工作并且 URL 正确，那么 r.status_code 应该返回 200，表示请求成功。


5. print(type(r.text))

输出 r.text 的数据类型。

r.text 是响应的文本内容，即网页的 HTML 源代码。

type(r.text) 应该返回 <class 'str'>，因为 r.text 是一个字符串类型的数据，表示网页内容的 HTML 文本。


6. print(r.text[:100])

打印响应内容的前 100 个字符。

r.text[:100] 表示取响应文本内容的前 100 个字符。网页内容通常是 HTML 格式，可以看到类似 <html、<head、<body 等标签。

（obsidian这里<>会导致无法渲染，因此只有一边<）

由于完整的网页 HTML 内容可能非常大，所以只取前 100 个字符进行预览。

7. print(r.cookies)

输出响应中的 cookies。

r.cookies 是一个 RequestsCookieJar 对象，包含了服务器在响应中设置的 cookies。

==Cookies 是服务器在用户浏览器中存储的一些小型数据，用于保存用户会话、个性化设置等信息。==

RequestsCookieJar 可以像字典一样使用，但也有其他方法，比如 get_dict() 将 cookies 转换为一个字典，或通过迭代访问每个 cookie 的键和值。

#### 那么get，post，put，delete，patch等请求是什么意思呢？

gpt：

在 HTTP 协议中，GET、POST、PUT、DELETE、PATCH 等请求方法（也称为 HTTP 动词）用于指定客户端（如浏览器或其他 HTTP 客户端）向服务器发送请求时的意图。每种方法对应不同类型的操作，下面是这些常见请求方法的详细解释：

1. GET（获取资源）

目的：用于从服务器获取资源。它请求的内容不会对服务器的数据产生影响，只是获取信息（例如，网页、图片、JSON 数据等）。

特点：

请求是安全的（不会修改服务器上的任何数据）。

请求是幂等的（多次请求相同的资源，结果相同）。

请求数据通常通过 URL 参数传递（例如：https://example.com/page?search=query）。


示例：

请求百度首页：GET https://www.baidu.com/



2. POST（提交数据）

目的：用于向服务器提交数据，通常用于创建资源或进行复杂的操作（如表单提交、文件上传等）。

特点：

不幂等（多次提交相同数据可能会导致不同的结果）。

通常请求体中包含数据，如表单数据、JSON 数据、文件等。

会对服务器数据产生影响，比如创建新资源、更新现有资源等。


示例：

提交表单数据：POST https://example.com/login，请求体可能包含用户名和密码。



3. PUT（更新资源）

目的：用于更新服务器上的资源，通常是完全替换指定资源的内容。

特点：

幂等性（多次发送相同的请求，结果是相同的）。

请求体包含要替换的资源数据。

一般用于替换指定路径下的资源，通常需要提供完整的资源内容。


示例：

更新用户信息：PUT https://example.com/user/123，请求体中包含更新后的用户数据。



4. DELETE（删除资源）

目的：用于请求删除服务器上的指定资源。

特点：

幂等性（即使发送多次相同的删除请求，结果也不会改变，资源仍然不存在）。

请求不会有请求体，但可以通过 URL 指定要删除的资源。


示例：

删除一个特定的用户：DELETE https://example.com/user/123



5. PATCH（部分更新资源）

目的：用于部分更新资源，通常只传递需要更新的字段，而不是整个资源。

特点：

不同于 PUT，PATCH 是对现有资源的部分更新。

幂等性（如果两次 PATCH 请求传送相同的更新内容，结果是相同的）。

请求体通常包含部分更新的数据。


示例：

更新用户的电子邮件地址：PATCH https://example.com/user/123，请求体中只包含更新后的电子邮件字段。



6. 其他常见的 HTTP 方法

虽然 GET、POST、PUT、DELETE 和 PATCH 是最常见的 HTTP 方法，但还有一些其他方法：

OPTIONS：用于询问服务器支持哪些 HTTP 方法。

HEAD：类似 GET，但是服务器只返回响应头，不返回响应体。常用于获取元数据。

TRACE：用于追踪请求经过的路径，通常用于调试。

CONNECT：用于将请求代理到指定的服务器，常用于建立安全隧道（例如用于 HTTPS）。


总结

GET：获取资源（无副作用）。

POST：提交数据（可能创建或更新资源）。

PUT：完全替换资源。

DELETE：删除资源。

PATCH：部分更新资源。

#### get请求

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

那么接下来就是豆瓣的那个案例，豆瓣的网站如下：

`https://movie.douban.com/`

目标是什么？目标是爬取电影。

![[Pasted image 20241109165718.png]]

操作如上，可以看到url，是get请求，和返回数据类型为json。

移动到payload处，可以看到有以下的请求：

![[Pasted image 20241109165824.png]]

所以在param里，我们需要这些请求

代码如下：

```
import requests  
import json  
  
if __name__=='__main__':  
    headers={  
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'  
    }  
    url="https://movie.douban.com/j/chart/top_list?"  
  
    param={  
        'type': '24',  
        'interval_id': '100:90',  
        'action': '',  
        'start': '0',  
        'limit': '20'  
    }  
  
    response=requests.get(url=url,params=param,headers=headers)  
  
    list_data=response.json()  
  
    fp=open('1.3douban.json','w',encoding='utf-8')  
    json.dump(list_data,fp=fp,ensure_ascii=False)  
  
    print("over!")

```

kfc案例，肯德基官网如下：

`https://www.kfc.com.cn/kfccda/index.aspx`

操作如下：

![[Pasted image 20241109170744.png]]

获取url，并且注意到他是post请求，返回的是text

需要的param：

![[Pasted image 20241109170805.png]]

对比一下param和和网页，可以得知有两个数据需要我们输入，其一是cname，即你按照的是省份查询还是城市查询，其二就是在当前省份或者城市查询kfc数据

代码如下：

```
import requests  
  
if __name__ =='__main__':  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'  
    }  
    # 按照城市查询  
    post_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'  
    cname_input = input("按照城市/查询:")  
    keyword_input = input("餐厅关键字：")  
    param = {  
        'op': 'keyword',  
        'cname': cname_input,  
        'pid':'',  
        'keyword': keyword_input,  
        'pageIndex': '1',  
        'pageSize': '10',  
    }  
  
    response=requests.post(url=post_url,params=param,headers=headers)  
  
    page_text=response.text  
    filename='1.4'+cname_input+','+keyword_input+'.txt'  
  
    with open(filename, 'w', encoding='utf-8') as fp:  
        fp.write(page_text)  
    print("OK!")
```

输入：

```
按照城市/查询:北京
餐厅关键字：前门
OK!
```

输出见文件。

#### 最后是药监局，由于没有url，所以硬听（）

找到了一个比较平替的网站，用这个来试试水。

`https://jwch.fzu.edu.cn/jxtz.htm`

哈哈。

目标是爬取具体的数据，也就是说，现在给你一个列表，我需要爬取在这里这个链接点进去具体的数据。

如果只对当前页面发送请求，那么将会无法获取具体页面的数据，并不能由当前的url获取。

![[Pasted image 20241109173827.png]]

response内并没有具体的信息。

我们想拿到的数据是动态加载的，所以不能通过直接的爬取去拿下里面的数据。

接下来猜返回数据是不是阿贾克斯请求，验证了一下，确实是。

药监局的例子，使用唯一id和企业名称拼接而成，但是由于该页面是动态生成的，所以直接使用这种方法，也没办法通过这种方法获取。

因为详情页面的界面也是通过动态加载出来的，并且可以捕获到。

而详情数据post到的url是一样的，只有id不一样

所以只需要批量获取多家企业的id，然后将id和url形成一个完整的详情页面。

最后的代码分成两部 ，第一步是先获取id，第二部是通过id找出详情界面。


![[Pasted image 20241109174553.png]]

发现这个之后，到payload和response看一下

![[Pasted image 20241109174712.png]]

![[Pasted image 20241109174650.png]]

所以这里应该和药监局那个不同，这里可以是通过此处的阿贾克斯请求，和id，拼接处需要的url，最后获取的应该是

---

看到这里其实就可以对福大教务处下手了，我的思路是通过各个发布人，先到对应的发布处，如教研处，爬取教研处对应的id，封装到一个列表里。随后通过列表去拼接教研处具体的网页，并且获取数据（尚未获取附件），于是写出如下丐版代码（教研处第一页）：

```
import requests  
import re  
  
headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'  
}  
  
def normal_get_id(li,url):  
    response=requests.get(url=url,headers=headers).text  
    pattern=r'info/\d+/(\d+)\.htm'  
    li.extend(re.findall(pattern,response))  
  
def add_normal_url(agent,num):  
    return 'https://jwch.fzu.edu.cn/info/'+agent+'/'+num+'.htm'  
  
def normal_get_one_resorces(agent,url,resource_list):  
    dic={}  
  
    response=requests.get(url=url,headers=headers)  
    response.encoding='utf-8'  
    dic['agent']=agent  
    dic['title']=re.search(r'<title>(.*?)</title>',response.text).group(1)  
    dic['date']=re.search(r'<span class="xl_sj_icon">发布时间：(.*?)</span><span class="xl_sj_icon2">',response.text).group(1)  
    dic['url']=url  
  
    '''  
    这里检查网页源码有没有附件之后，使用阿贾克斯请求来获取附件的个数和下载次数  
    '''  
    resource_list.append(dic)  
  
    #提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。  
    #可能存在“附件”，提取附件名，附件下载次数，附件链接吗，有能力请尽可能将附件爬取下来。  
  
def normal_get_all_resorces(resource_list,num_list,agent):  
    for num in num_list:  
        url=add_normal_url(agent,num)  
        normal_get_one_resorces(agent,url,resource_list)  
  
if __name__ == '__main__':  
  
    zhk_agent = '1035'  
    jxyx_agent = '1036'  
  
    zhk_num_list = []  
    jxyx_num_list = []  
  
    zhk_url = 'https://jwch.fzu.edu.cn/jxtz/zhk.htm'  
    jxyx_url = 'https://jwch.fzu.edu.cn/jxtz/jxyx.htm'  
  
    zhk_resource_list=[]#封装一个列表，列表里的元素是字典  
    jxyx_resource_list=[]  
  
    #获取id  
    normal_get_id(zhk_num_list,zhk_url)  
  
  
    #获取数据  
    normal_get_all_resorces(zhk_resource_list,zhk_num_list,zhk_agent)  
  
  
    print(zhk_resource_list)
```

输出：

```
[{'agent': '1035', 'title': '关于召开2024-2025学年秋季学期期初本科教育教学工作会议的通知-福州大学教务处', 'date': '2024-09-06', 'url': 'https://jwch.fzu.edu.cn/info/1035/13666.htm'}, {'agent': '1035', 'title': '关于2024-2025学年第一学期本科生学生证和火车票优惠区间更改的通知-福州大学教务处', 'date': '2024-09-04', 'url': 'https://jwch.fzu.edu.cn/info/1035/13654.htm'}, {'agent': '1035', 'title': '关于召开2024年宁夏大学、银川能源学院本科生赴福州大学访学见面交流会的通知-福州大学教务处', 'date': '2024-09-02', 'url': 'https://jwch.fzu.edu.cn/info/1035/13651.htm'}, {'agent': '1035', 'title': '关于2024级本科生（含访学学生）学生证信息采集的通知-福州大学教务处', 'date': '2024-09-02', 'url': 'https://jwch.fzu.edu.cn/info/1035/13648.htm'}, {'agent': '1035', 'title': '关于购买优惠火车票相关事宜的通知-福州大学教务处', 'date': '2024-08-30', 'url': 'https://jwch.fzu.edu.cn/info/1035/13646.htm'}, {'agent': '1035', 'title': '教务处关于2024年暑假用印安排的通知-福州大学教务处', 'date': '2024-07-06', 'url': 'https://jwch.fzu.edu.cn/info/1035/13626.htm'}, {'agent': '1035', 'title': '友情提示-福州大学教务处', 'date': '2024-06-29', 'url': 'https://jwch.fzu.edu.cn/info/1035/13592.htm'}, {'agent': '1035', 'title': '关于2023-2024学年第二学期再次开放本科生学生证和火车票优惠卡补办及火车票优惠卡更改区间的通知-福州大学教务处', 'date': '2024-05-08', 'url': 'https://jwch.fzu.edu.cn/info/1035/13475.htm'}, {'agent': '1035', 'title': '关于第61届中国高等教育博览会的参会指南-福州大学教务处', 'date': '2024-04-12', 'url': 'https://jwch.fzu.edu.cn/info/1035/13378.htm'}, {'agent': '1035', 'title': '关于组织教师参加第61届中国高等教育博览会的通知-福州大学教务处', 'date': '2024-04-02', 'url': 'https://jwch.fzu.edu.cn/info/1035/13347.htm'}, {'agent': '1035', 'title': '关于更改2023-2024学年春季学期期初本科教育教学工作会议时间的通知-福州大学教务处', 'date': '2024-03-14', 'url': 'https://jwch.fzu.edu.cn/info/1035/13313.htm'}, {'agent': '1035', 'title': '关于召开2023-2024学年春季学期期初本科教育教学工作会议的通知-福州大学教务处', 'date': '2024-03-13', 'url': 'https://jwch.fzu.edu.cn/info/1035/13309.htm'}, {'agent': '1035', 'title': '关于2023-2024学年第二学期本科生学生证和火车票优惠卡补办及火车票优惠卡更改区间的通知-福州大学教务处', 'date': '2024-02-29', 'url': 'https://jwch.fzu.edu.cn/info/1035/13280.htm'}, {'agent': '1035', 'title': '教务处关于2024年寒假用印安排的通知-福州大学教务处', 'date': '2024-01-20', 'url': 'https://jwch.fzu.edu.cn/info/1035/13252.htm'}, {'agent': '1035', 'title': '关于召开2023-2024学年秋季学期期末本科教育教学工作会议的通知-福州大学教务处', 'date': '2024-01-10', 'url': 'https://jwch.fzu.edu.cn/info/1035/13242.htm'}, {'agent': '1035', 'title': '关于2023-2024学年第一学期再次开放本科生学生证和火车票优惠卡补办及火车票优惠卡更改区间的通知-福州大学教务处', 'date': '2023-11-14', 'url': 'https://jwch.fzu.edu.cn/info/1035/13132.htm'}, {'agent': '1035', 'title': '关于福州大学智慧教室二期使用培训的通知-福州大学教务处', 'date': '2023-10-24', 'url': 'https://jwch.fzu.edu.cn/info/1035/13062.htm'}, {'agent': '1035', 'title': '关于召开2023-2024学年秋季学期期初本科教育教学工作会议的通知-福州大学教务处', 'date': '2023-09-01', 'url': 'https://jwch.fzu.edu.cn/info/1035/12955.htm'}, {'agent': '1035', 'title': '关于2023-2024学年第一学期本科生学生证和火车票优惠卡补办及火车票优惠卡更改区间的通知-福州大学教务处', 'date': '2023-08-27', 'url': 'https://jwch.fzu.edu.cn/info/1035/12937.htm'}, {'agent': '1035', 'title': '关于2023级福州大学本科生学生证信息采集的通知-福州大学教务处', 'date': '2023-08-27', 'url': 'https://jwch.fzu.edu.cn/info/1035/12934.htm'}]
```

在完成上述丐版代码的同时，我也在思考如何获取附件。此时阿贾克斯请求的作用就出来了！

而最后封装到c啥的那个文件，利用的是pandas库，比较基本的东西。

总的来说，只需要学最基本的爬虫知识，就可以完成对福大教务处的爬取。

----

好，既然学完了最基础的，直接开始写最难的。

目前为止还差最后一个教材中心没爬，暂且的代码如下：

```
import requests  
import re  
import pandas as pd  
  
  
  
headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'  
}  
  
def normal_get_id(li,url):  
    response=requests.get(url=url,headers=headers).text  
    pattern=r'info/\d+/(\d+)\.htm'  
    li.extend(re.findall(pattern,response))  
  
def add_normal_url(agent,num):  
    return 'https://jwch.fzu.edu.cn/info/'+agent+'/'+num+'.htm'  
  
def get_id(agent,num_list,url,num,ch):  
    normal_get_id(num_list,url)  
    num-=1  
    while num>=1:  
        current_url='https://jwch.fzu.edu.cn/jxtz/'+ch+'/'+str(num)+'.htm'  
        response=requests.get(url=current_url,headers=headers).text  
        pattern = r'info/\d+/(\d+)\.htm'  
        num_list.extend(re.findall(pattern, response))  
        num-=1  
  
  
def normal_get_one_resorces(agent,url,resource_list):  
    dic={}  
  
    response=requests.get(url=url,headers=headers)  
    response.encoding='utf-8'  
  
    dic['agent']=agent  
    dic['title']=re.search(r'<title>(.*?)</title>',response.text).group(1)  
    data_resorce=(re.search(r'发布时间：(.*?)</span>',response.text))  
    if  data_resorce:  
        dic['date']=data_resorce.group(1)  
    dic['url']=url  
  
    '''  
    这里检查网页源码有没有附件之后，使用阿贾克斯请求来获取附件的个数和下载次数  
    '''    dic['attachment']={}  
    dic['attachment']['url']=[]  
    dic['attachment']['name']=[]  
    dic['attachment']['webfile_id']=[]  
    dic['attachment']['times'] = []  
  
    pattern = r'info/\d+/(\d+)\.htm'  
  
    match_response=re.findall(r'a href="(/system/_content/download.jsp\?urltype=news.DownloadAttachUrl&owner=1744984858&wbfileid=(.*?))" target="_blank">(.*?)</a>',response.text)  
  
    for url, webfile_id, name in match_response:  
        dic['attachment']['url'].append(url)  
        dic['attachment']['webfile_id'].append(webfile_id)  
        dic['attachment']['name'].append(name)  
  
    for id in dic['attachment']['webfile_id']:  
        file_url='https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid='+id+'&owner=1744984858&type=wbnewsfile&randomid=nattach'  
        response_id=requests.get(url=file_url,headers=headers).text  
        times_match=re.search(r'{"wbshowtimes":(\d+),',response_id).group(1)  
        dic['attachment']['times'].append(times_match)  
  
    resource_list.append(dic)  
  
    #提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。  
    #可能存在“附件”，提取附件名，附件下载次数，附件链接吗，有能力请尽可能将附件爬取下来。  
  
def normal_get_all_resorces(resource_list,num_list,agent):  
    for num in num_list:  
        url=add_normal_url(agent,num)  
        normal_get_one_resorces(agent,url,resource_list)  
  
if __name__ == '__main__':  
  
    zhk_agent = '1035'  
    jxyx_agent = '1036'  
    jyjg_agent= '1037'  
    jhk_agent='1038'  
    sjk_agent='1039'  
    zlb_agent='1040'  
    tpxqglk_agent='1152'  
  
    #这里还差一个教材中心  
  
    zhk_num_list = []  
    jxyx_num_list = []  
    jyjg_num_list=[]  
    jhk_num_list=[]  
    sjk_num_list=[]  
    zlb_num_list=[]  
    tpxqglk_num_list=[]  
  
    zhk_url = 'https://jwch.fzu.edu.cn/jxtz/zhk.htm'  
    jxyx_url = 'https://jwch.fzu.edu.cn/jxtz/jxyx.htm'  
    jyjg_url='https://jwch.fzu.edu.cn/jxtz/jyjg.htm'  
    jhk_url='https://jwch.fzu.edu.cn/jxtz/jhk.htm'  
    sjk_url='https://jwch.fzu.edu.cn/jxtz/sjk.htm'  
    zlb_url='https://jwch.fzu.edu.cn/jxtz/zlb.htm'  
    tpxqglk_url='https://jwch.fzu.edu.cn/jxtz/tpxqglk.htm'  
  
    zhk_resource_list=[]#封装一个列表，列表里的元素是字典  
    jxyx_resource_list=[]  
    jyjg_resource_list=[]  
    jhk_resource_list=[]  
    sjk_resource_list=[]  
    zlb_resource_list=[]  
    tpxqglk_resource_list=[]  
  
    #获取id  
    get_id(zhk_agent,zhk_num_list,zhk_url,20,'zhk')  
    get_id(jxyx_agent,jxyx_num_list,jxyx_url,80,'jxyx')  
    get_id(jyjg_agent,jyjg_num_list,jyjg_url,22,'jyjg')  
    get_id(jhk_agent,jhk_num_list,jhk_url,10,'jhk')  
    get_id(sjk_agent,sjk_num_list,sjk_url,45,'sjk')  
    get_id(zlb_agent,zlb_num_list,zlb_url,17,'zlb')  
    get_id(tpxqglk_agent,tpxqglk_num_list,tpxqglk_url,4,'tpxqglk')  
  
  
    #获取数据  
    normal_get_all_resorces(zhk_resource_list,zhk_num_list,zhk_agent)  
    normal_get_all_resorces(jxyx_resource_list,jxyx_num_list,jxyx_agent)  
    normal_get_all_resorces(jyjg_resource_list,jyjg_num_list,jyjg_agent)  
    normal_get_all_resorces(jhk_resource_list,jhk_num_list,jhk_agent)  
    normal_get_all_resorces(sjk_resource_list,sjk_num_list,sjk_agent)  
    normal_get_all_resorces(zlb_resource_list,zlb_num_list,zlb_agent)  
    normal_get_all_resorces(tpxqglk_resource_list,tpxqglk_num_list,tpxqglk_agent)  
  
    all_list=(zhk_resource_list+jxyx_resource_list+jyjg_resource_list+  
              jhk_resource_list+sjk_resource_list+zlb_resource_list+  
              tpxqglk_resource_list)  
  
    df=pd.json_normalize(all_list,sep='_')  
  
    df=df.explode(['attachment_url',  
                   'attachment_name',  
                   'attachment_webfile_id',  
                   'attachment_times']).reset_index(drop=True)  
  
    df.to_csv("fzu_edu.csv",index=False)  
  
    print("ok")
```

附件还没有下载，这里panda的操作由部分是ai的，实在太困了，写到两点多了。

输出见附件。