# coding:utf-8
from util.operation_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse
from util.operation_json import OperationJson
from util.operation_header import OperationHeader
import json


class DependdentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        headers = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        if headers=='write':
            res= run_method.run_main(method,url,request_data)
            op_header=OperationHeader(res)
            op_header.write_cookie()
        elif headers=='yes':
            op_json=OperationJson('../config/cookie.json')
            # apsid是cookie的字段，根据具体项目修改
            cookie=op_json.get_json_data('apsid')
            cookies={
                'apsid':cookie
            }
            res = run_method.run_main(method, url, request_data, cookies)
        else:
            res=run_method.run_main(method,url,request_data)
        # jsonpath需要转换的类型是json，所以需要将res转换成json格式
        return json.loads(res)

    # 根据依赖的key，去返回值中提取需要的数据
    def get_data_for_depend_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        # jsonpath需要转换的类型是json，所以需要将res转换成json格式
        # print type(depend_data)
        # print type(response_data)
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
