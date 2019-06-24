# coding:utf-8
from base.run_method import RunMethod
from data.get_data import GetData
from util.commom_util import CommonUtil


class RunTest(object):
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util=CommonUtil()

    # 程序执行
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            request_data = self.data.get_data_for_json(i)
            expect_result=self.data.get_expect_data(i)
            headers = self.data.is_header(i)
            # print(url,method,is_run,request_data,headers)
            if is_run:
                res = self.run_method.run_main(method, url, request_data, headers)
                print(expect_result)
                print(res)
                if self.common_util.is_contain(expect_result,res):
                    print("测试成功")
                else:
                    print("测试失败")


if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
