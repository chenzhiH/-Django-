import json
import requests
import urllib.error
import urllib.request
import re
from utils import proxy

def weather(cityname):
    key = 'f160cede132a35fc800e7ca70ee267fc'
    api = 'http://v.juhe.cn/weather/index'
    params = 'cityname=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    response = requests.get(url=url)
    data = json.loads(response.text)
    result = data.get('result')
    sk = result.get('sk')
    response = {}
    response['temperature'] = sk.get('temp')
    response['wind_direction'] = sk.get('wind_direction')
    response['wind_strength'] = sk.get('wind_strength')
    response['humidity'] = sk.get('humidity')  # 湿度
    response['time'] = sk.get('time')
    return response

def stock(market,code):
    proxy_addr = "218.85.22.216:9999"
    proxy = urllib.request.ProxyHandler({"https": proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    url = "http://hq.sinajs.cn/list=%s" % (code)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0'
    })
    data = urllib.request.urlopen(req).read()
    a = data.hex()
    m = 0
    m2 = 0
    m3 = 0
    response={
        'name':market
    }
    for i in range(70):
        c = data[i]
        if (c == 44):
            m2=m
            m=i
            m3= m3+1;
            if(m3==2):
                response['start_price']=data[m2+1:m-1].decode('ascii')
            elif(m3==3):
                response['now_price']=data[m2+1:m-1].decode('ascii')
            elif (m3 == 4):
                response['today_max'] = data[m2 + 1:m - 1].decode('ascii')
            elif (m3 == 5):
                response['today_min'] = data[m2 + 1:m - 1].decode('ascii')
                break


    # response = {
    #     'name': market,
    #     'now_price': data[m + 15:m + 21].decode('ascii'),
    #     'today_min': data[m + 29:m + 35].decode('ascii'),
    #     'today_max': data[m + 22:m + 28].decode('ascii'),
    #     'start_price': data[m + 1:m + 7].decode('ascii'),
    #     # 'date': data.get('date'),
    #     # 'time': data.get('time')
    # }

    response['is_rising'] = response['now_price'] >= response['start_price']
    sub = abs(float(response['now_price']) - float(response['start_price']))  # 差值
    response['sub'] = float('%.3f' % sub)
    print(response)
    return response

def xingzuo(conse):
    constellations = {'白羊座': "aries/", '金牛座': 'taurus/', '双子座': 'gemini/', '巨蟹座': 'cancer/', '狮子座': 'leo/',
                      '处女座': 'virgo/', '天秤座': 'libra/', '天蝎座': 'scorpio/', '射手座': 'sagittarius/', '摩羯座': 'capricorn/',
                      '水瓶座': 'aquarius/', '双鱼座': 'pisces/'}
    proxy_addr = "163.125.235.128:8118"
    proxy = urllib.request.ProxyHandler({"https": proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    reponse = {}
    url = "http://www.xzw.com/fortune/" + constellations[conse]
    print(url)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    })
    data = urllib.request.urlopen(req)
    data = data.read().decode("utf-8", "ignore")
    pat = '<meta name="description" content="(.*?)" />'
    number = re.compile(pat).findall(data)
    reponse['name'] = conse
    reponse['text'] = number
    return reponse


def joke():
    proxy_addr = "14.23.58.58:443"
    proxy = urllib.request.ProxyHandler({"http": proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

    url = "https://www.qiushibaike.com/text/"
    print(url)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    })
    data = urllib.request.urlopen(req)
    data = data.read().decode("utf-8", "ignore")
    data1 = []
    pat = '<div class="content">\n<span>(.*?)</span>'
    number = re.compile(pat, re.S).findall(data)
    for i in number:
        reponse = {}
        i = i.replace('\n', '')
        i = i.replace('<br/>', '\n')
        reponse['text'] = i
        data1.append(reponse)
    return data1

if __name__=="__main__":
    data=joke()
    print(data)