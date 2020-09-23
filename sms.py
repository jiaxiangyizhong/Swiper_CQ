import json
import time
from hashlib import md5

import requests


def sms():
    appid = '48182'
    appkey = '15d3274309e4a031e766d3f91835c94c'

    args = {
        'appid': '48182',  # APPID
        'to': '13021607300',  # 手机号
        'project': '2OuxR3',  # 短信模板的 ID
        'vars': json.dumps({'vcode': '123456'}),
        'timestamp': int(time.time()),
        'sign_type': 'md5',
    }

    api = 'https://api.mysubmail.com/message/xsend.json'

    # 计算参数的签名
    sorted_args = sorted(args.items())  # 提取每一项
    args_str = '&'.join([f'{key}={value}' for key, value in sorted_args])  # 对参数排序、组合
    sign_str = f'{appid}{appkey}{args_str}{appid}{appkey}'.encode('utf8')  # 拼接成待签名字符串
    signature = md5(sign_str).hexdigest()  # 计算签名
    args['signature'] = signature

    response = requests.post(api, data=args)
    print('状态码：', response.status_code)

    result = response.json()
    print('短信结果：', result)