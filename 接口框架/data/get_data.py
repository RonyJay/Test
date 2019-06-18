# coding:utf-8
from util.operation_excel import OperationExcel
import data_config


# 获取到excel数据后的预处理
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

    #是否携带header
    def is_header(self,row):
        col = int(data_config.globla_var.get_header())
