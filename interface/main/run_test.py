# coding:utf-8
import sys

sys.path.append('..')
sys.path.append('..\\base')
sys.path.append('..\\data')
sys.path.append('..\\dataconfig')
sys.path.append('..\\main')
sys.path.append('..\\util')

from base.run_method import RunMethod
from data.get_data import GetData
from util.commom_util import CommonUtil
from data.depend_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson


class RunTest(object):
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.send_email = SendEmail()

    # 程序执行
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect_result = self.data.get_expect_data(i)
                headers = self.data.is_header(i)
                depend_case = self.data.get_case_id_depend(i)
                '''
                判断依赖情况
                '''
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_depend_key(i)
                    # 获取数据依赖的字段
                    depend_field = self.data.get_field_depend(i)
                    # 更新request_data字段
                    request_data[depend_field] = depend_response_data
                '''
                判断headers情况
                write yes no
                '''
                if(headers=='write'):
                    res=self.run_method.run_main(method,url,request_data)
                    op_heaer=OperationHeader(res)
                    op_heaer.write_cookie()
                elif headers=='yes':
                    op_json = OperationJson('../dataconfig/cookie.json')
                    #apsid是cookie的字段，根据具体项目修改
                    cookie=op_json.get_json_data('apsid')
                    cookies={
                        'apsid':cookie
                    }
                    res=self.run_method.run_main(method,url,request_data,cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)
                '''
                写入测试结果
                '''
                if self.common_util.is_contain(expect_result, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
        self.send_email.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
