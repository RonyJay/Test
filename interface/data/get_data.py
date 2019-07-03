# coding:utf-8
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from data_config import globla_var


# 获取到excel数据,进行初步的处理
class GetData(object):
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.globla = globla_var()

    # 获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        # col = int(data_config.get_run())
        col = int(self.globla.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(self.globla.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        # col = int(data_config.get_request_way())
        col = int(self.globla.get_request_way())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 获取url
    def get_request_url(self, row):
        # col = int(data_config.get_url())
        col = int(self.globla.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取json_key
    def get_json_key(self, row):
        # col = int(data_config.get_json_key())
        col = int(self.globla.get_json_key())
        key = self.opera_excel.get_cell_value(row, col)
        if key == '':
            return None
        return key

    # 通过key获取到json数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_json_data(self.get_json_key(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        # col = int(data_config.get_expect())
        col = int(self.globla.get_expect())
        expect_data = self.opera_excel.get_cell_value(row, col)
        if expect_data == '':
            return None
        return expect_data

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = int(self.globla.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 判断是否有case依赖
    def get_case_id_depend(self, row):
        col = int(self.globla.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_field_depend(self, row):
        col = int(self.globla.get_field_depend())
        depend_field = self.opera_excel.get_cell_value(row, col)
        if depend_field == "None":
            return None
        else:
            return depend_field

    # 写入实际结果
    def write_result(self, row, value):
        col = int(self.globla.get_result())
        return self.opera_excel.write_value(row, col, value)
