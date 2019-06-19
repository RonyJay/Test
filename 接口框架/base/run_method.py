# coding:utf-8
import requests


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if (header != None):
            requests.post(url=url, data=data, headers=header).json()
        else:
            requests.post(url=url, data=data).json()
        return res

    def get_main(self, url, data, header):
        res = None
        if (header != None):
            requests.get(url=url, data=data, headers=header).json()
        else:
            requests.get(url=url, data=data).json()
        return res

    def run_main(self, method, url, data, header):
        pass
