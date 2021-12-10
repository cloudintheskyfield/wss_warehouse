from django.http import HttpResponse, JsonResponse
import json

from django.views import View


def response_views(request):
    # response = JsonResponse()
    # return response
    info = {
        'name': 'itcast',
        'address': 'shunyi'
    }
    girl_friends = [
        {
            'name': '小美'
        },
        {
            'name': '李玉'
        }
    ]
    # safe = True 表示的我们的data为字典数据
    # JsonResponse 可以把字典转换为Json
    # JsonResponse data传递的是字典数据

    # json.loads --->json字符串转换为字典
    # json.dumps--->将字典转换为字符串
    data = json.dumps(girl_friends)
    response = HttpResponse(data)
    # response = JsonResponse(data=girl_friends, safe=False)
    return response


# 判断只有登录用户才可以访问页面
from django.contrib.auth.mixins import LoginRequiredMixin
# LoginRequiredMixin
class OrderView(View):

    def get(self, request):
        # 1. 该处可以用装饰器判断
        # 2. 该处还可以使用多继承判断
        is_login = False
        if not is_login:
            return HttpResponse('你没有登录，跳转到整理页面中')
        return HttpResponse('GET 我的订单页面，这个页面必须登录')

    def post(self, request):
        return HttpResponse('POST 我的订单页面 这个页面必须登录')






















