import requests

if __name__ == '__main__':
    #制定url
    url='http://www.sogou.com/'
    response=requests.get(url=url)
    page_text=response.text
    print(page_text)