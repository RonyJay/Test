# coding:utf-8
from base.run_method import RunMethod
from data.get_data import GetData
from util.commom_util import CommonUtil
from data.depend_data import DependdentData
from util.send_email import SendEmail


class RunTest(object):
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.send_email=SendEmail()

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
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_depend_key(i)
                    # 获取数据依赖的字段
                    depend_field = self.data.get_field_depend(i)
                    # 更新request_data字段
                    request_data[depend_field] = depend_response_data
                res = self.run_method.run_main(method, url, request_data, headers)
                if self.common_util.is_contain(expect_result, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
        self.send_email.send_main(pass_count,fail_count)


if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
