import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from authorization.models import User
from utils.response import CommonResponseMixin,ReturnCode
from thirdparty import juhe
import utils

class weatherView(View,CommonResponseMixin):
    def get(self,request):
        if not utils.auth.already_authorized(request):
            respone=self.wrap_json_response({},code=ReturnCode.UNAUTHORIZED)
        else:
            data=[]
            open_id=request.session.get('open_id')
            user=User.objects.filter(open_id=open_id)
            city = user[0].focus_cities
            city = eval(city)
            for cities in city:
                result=juhe.weather(cities.get('city'))
                result['city_info']=cities
                data.append(result)
            respone = self.wrap_json_response(data=data, code=ReturnCode.UNAUTHORIZED)
        return JsonResponse(data=respone,safe=False)
    def post(self,request):
        data=[]
        received_body=request.body.decode('utf-8')
        received_body=json.loads(received_body)
        cities=received_body.get('cities')
        for citie in cities:
            print(citie["city"])
            result = juhe.weather(citie["city"])
            result['city_info']=citie
            data.append(result)
        data=self.wrap_json_response(data=data)

        return JsonResponse(data=data,safe=False)