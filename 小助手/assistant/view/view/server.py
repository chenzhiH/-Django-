import json
from django.views import View
from django.http import HttpResponse, JsonResponse
import utils
from utils.response import CommonResponseMixin,ReturnCode
from thirdparty import juhe
from django.core.cache import cache
from utils.timeutil import get_day_left_in_second
import logging

popular_stocks = [
    {
        'code':'000001',
        'name':'平安银行',
        'market':'sz'
    },
    {
        'code':'000002',
        'name':'万科A',
        'market':'sz'
    },
    {
        'code':'600036',
        'name':'招商银行',
        'market':'sh'
    },
    {
        'code':'601398',
        'name':'工商银行',
        'market':'sh'
    }
]

def stock(request):
    data=[]
    stocks=[]
    if utils.auth.already_authorized(request):
        user=utils.auth.get_user(request)
        stocks = user[0].focus_stock
        stocks = eval(stocks)
    else:
        stocks=popular_stocks
    for stock in stocks:
        u=stock['market']+stock['code']
        result=juhe.stock(stock['name'],u)
        data.append(result)
    reponse= CommonResponseMixin.wrap_json_response(data=data,code=ReturnCode.SUCCESS)
    return JsonResponse(data=reponse,safe=False)

def constellation(request):
    if utils.auth.already_authorized(request):
        user=utils.auth.get_user(request)
        constellations = user[0].focus_constellations
        constellations = eval(constellations)
    else:
        constellations = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
    data = []
    for i in constellations:
        result=cache.get(i)
        if not result:
            result=juhe.xingzuo(i)
            timeout=get_day_left_in_second()
            cache.set(i,result,timeout)
            logging.info("set code key=[%s],value=[%s],timeout=[%d]"%(i,result,timeout))
        data.append(result)
    reponse= CommonResponseMixin.wrap_json_response(data=data,code=ReturnCode.SUCCESS)
    return JsonResponse(data=reponse,safe=False)

def joke(request):
    data=juhe.joke()
    reponse = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(data=reponse, safe=False)

