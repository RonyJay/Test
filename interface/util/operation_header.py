# coding:utf-8
import requests
import json
from util.operation_json import OperationJson

'''
此文件只是提供了cookie相关操作的思路
应用到项目中，需要根据项目的情况再具体改造
'''


class OperationHeader:
    def __init__(self, response):
        self.response = json.loads(response)

    # 获取登录返回的token的url
    def get_response_url(self):
        url = self.response['data']['url'][0]
        return url

    # 获取cookie的jar文件
    def get_cookie(self):
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    # 将cookie写入json中
    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperationJson()
        op_json.write_data(cookie)


if __name__ == '__main__':
    url = "http://m.imooc.com/passport/user/login"
    data = {
        "username": "18513199586",
        "password": "111111",
        "verify": "",
        "referer": "https://m.imooc.com"
    }
    res = json.dumps(requests.post(url, data).json())
    op_header = OperationHeader(res)
    op_header.write_cookie()
