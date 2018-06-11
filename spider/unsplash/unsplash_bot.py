# coding = utf-8

import requests

def un_spider():
    headers = {
        'Referer': 'https://unsplash.com/',
        'Accept': '* / *',
        'Connection': 'keep-alive',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'Host': 'unsplash.com',
        'Authorization': 'Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09',

    }
    url = 'https://unsplash.com/napi/feeds/home?after=bf2eaef0-45f2-11e8-8080-80006e9768fc'
    response = requests.get(url=url,headers=headers,verify = False)
    print(response.content)
    with open("unsplash.html",'w') as f:
        f.write(response.content)


if __name__ == '__main__':
    un_spider()

