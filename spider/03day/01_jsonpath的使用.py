# -*- coding:utf-8 -*-
import requests
import json
import jsonpath


def getcity():
    url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36" }
    # 这样会保存cookie
    #requests.session(url)

    #   resp.text返回的是Unicode型的数据。
    # resp.content返回的是bytes型也就是二进制的数据
    response = requests.get(url,headers=headers).text

    #print response
    #response.headers.update(headers)

    #把Json格式字符串解码转换成Python对象 string会转为unicode编码的格式
    json_city  = json.loads(response)

    # 得到的是unicode的list
    city_list = jsonpath.jsonpath(json_city,"$..name")

    print len(city_list)

    for city in city_list:
        print city


    #实现python类型转化为json字符串，返回一个str对象  list--->array
    # 注意：json.dumps() 序列化时默认使用的ascii编码
    # 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
    city_array = json.dumps(city_list,ensure_ascii=False)
    with open("city.json","w") as f:
        f.write(city_array.encode("utf-8"))





if __name__ == '__main__':
    getcity()