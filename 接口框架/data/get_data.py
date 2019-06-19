# coding:utf-8
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
import data_config


# 获取到excel数据,进行初步的处理
class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # 获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.globla_var.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(data_config.globla_var.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.globla_var.get_request_way())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 获取url
    def get_request_url(self, row):
        col = int(data_config.globla_var.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取json_key
    def get_json_key(self, row):
        col = int(data_config.globla_var.get_json_key())
        key = self.opera_excel.get_cell_value(row, col)
        if key == '':
            return None
        return key

    # 通过key获取到json数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_json_data(self.get_json_key(row))
        return request_data

    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.globla_var.get_expect())
        expect_data = self.opera_excel.get_cell_value(row,col)
        if expect_data=='':
            return None
        return expect_data