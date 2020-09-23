'程序逻辑配置，及第三方平台配置'
import json

appid = '48182'
appkey = '15d3274309e4a031e766d3f91835c94c'
project= '2OuxR3'  # 短信模板的 ID
vars=json.dumps({'vcode': '123456'})
sign_type='md5'


api = 'https://api.mysubmail.com/message/xsend.json'