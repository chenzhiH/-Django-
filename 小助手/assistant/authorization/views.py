from django.shortcuts import render
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from utils.auth import c2s,already_authorized
from utils.response import CommonResponseMixin,ReturnCode
from .models import User,Eshi
import re
# Create your views here.

#这里是保存和返回使用者关注的信息

class UserView(View,CommonResponseMixin):
    def get(self,request):  #获取数据并返回
        if not already_authorized(request):
            response=self.wrap_json_response(code=ReturnCode.SUCCESS)
            return JsonResponse(data=response,safe=False)
        open_id=request.session.get('open_id') #获取session信息
        user = User.objects.filter(open_id=open_id)#获取数据库信息
        data = {}
        data['open_id'] = user[0].open_id
        data['focus'] = {}
        constellation=user[0].focus_constellations  #将星座，股票，城市信息装换成数组形式（列表）形式
        constellation=eval(constellation)
        stock = user[0].focus_stock
        stock=eval(stock)

        city = user[0].focus_cities
        city = eval(city)

        data['focus']['city'] = city
        data['focus']['constellation'] = constellation
        data['focus']['stock'] = stock

        response = self.wrap_json_response(code=ReturnCode.SUCCESS, data=data)
        return JsonResponse(response, safe=False)
    def post(self,request):
        if not already_authorized(request):# 判断是否授权
            response=self.wrap_json_response(code=ReturnCode.SUCCESS)
            return JsonResponse(data=response,safe=False)
        open_id=request.session.get('open_id') # 获取该用户的唯一标识
        user = User.objects.get(open_id=open_id)# 获取该用户的关注信息
        received_body=request.body.decode('utf-8')  #取出从微信端返回的信息
        received_body=eval(received_body) # 将用户信息字典化
        cities=received_body.get('city')
        stocks=received_body.get('stock')
        constellations=received_body.get('constellation')
        user.focus_cities=cities  #将返回的信息重新复制到数据库中
        user.focus_stock=stocks
        user.focus_constellations=constellations
        user.save()  #保存到数据库中
        response=self.wrap_json_response(code=ReturnCode.SUCCESS,message='modify user info sucess')
        return JsonResponse(data=response,safe=False)

def test_session(request):
    request.session['message'] = 'Test Django Session OK!'  #判断返回的信息是否为唯一标志，返回确定
    response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)

# def test_session2(request):
#     print("session content",request.session.items())
#     response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS)
#     return JsonResponse(data=response, safe=False)

def _authorize_by_code(request):
    post_data=request.body.decode('utf-8')
    post_data=json.loads(post_data)
    code=post_data.get('code').strip()
    app_id = post_data.get('appId').strip()
    nickname = post_data.get('nickname').strip()
    respone={}
    if not code or not app_id:
        respone['message']='authorized failed,need entire authorization data'
        respone['code']=ReturnCode.BROKEN_AUTHORIZED_DATA
        return JsonResponse(data=respone,safe=False)
    data=c2s(app_id,code)
    openid=data.get('openid')
    if not openid:
        respone=CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS,message='auth failed')
        return JsonResponse(data=respone,safe=False)
    request.session['open_id']=openid
    request.session['is_authorized']=True
    if not User.objects.filter(open_id=openid):
        new_user=User(open_id=openid,nickname=nickname)
        new_user.save()

    respone=CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS,message='auth success')
    return JsonResponse(data=respone,safe=False)

def authorize(request):
    return  _authorize_by_code(request)

def get_status(request):
    print('call get_status function...')
    if already_authorized(request):
        data = {"is_authorized": 1}
    else:
        data = {"is_authorized": 0}
    response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(response, safe=False)

def logout(request):
    '''
    注销，小程序删除存储的Cookies
    '''
    request.session.clear()
    response = {}
    response['result_code'] = 0
    response['message'] = 'logout success.'
    return JsonResponse(response, safe=False)