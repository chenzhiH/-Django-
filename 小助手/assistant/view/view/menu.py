import os,sys
import yaml

from django.http import JsonResponse

from assistant import settings
import utils.response
def init_app_data():
    data_file=os.path.join(settings.BASE_DIR,'D://python代码/Django/assistant/view/view/app.yaml')
    with open(data_file,'r',encoding='utf-8') as f:
        app = yaml.load(f)
        return app

def get_menu(request):
    global_app_data=init_app_data()
    public_app_data=global_app_data.get('published')
    response=utils.response.wrap_json_response(data=public_app_data,code=utils.response.ReturnCode.SUCCESS)
    return JsonResponse(data=response,safe=False)