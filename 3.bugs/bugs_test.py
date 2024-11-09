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

