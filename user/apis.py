from django.http import JsonResponse
from user.logics import send_vcode

def fetch_vcode(request):
    "给用户发送验证码"
    phonenum=request.GET.get('phonrnum')
    if send_vcode(phonenum):
        return JsonResponse({'code':0,'data':None})
    else:
        return JsonResponse({'code': 1000, 'data': None})

def submit_vcode(request):
    return JsonResponse

def show_profiles(request):
    return JsonResponse

def update_profiles(request):
    return JsonResponse
def qn_token(request):
    return JsonResponse

def fetch_vcode(request):
    return JsonResponse


