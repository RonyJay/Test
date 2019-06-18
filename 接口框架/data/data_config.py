# coding:utf-8
class globla_var:
    # case_id
    id = '0'
    url = '1'
    run = '2'
    request_way = '3'
    header = '4'
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    data = '8'
    expect = '9'
    result = '10'

    # 获取caseid
    def get_id(self):
        return globla_var.id

    def get_url(self):
        return globla_var.url

    def get_run(self):
        return globla_var.run

    def get_request_way(self):
        return globla_var.request_way

    def get_header(self):
        return globla_var.get_header

    def get_case_depend(self):
        return globla_var.case_depend

    def get_data_depend(self):
        return globla_var.data_depend

    def get_field_depend(self):
        return globla_var.field_depend

    def get_data(self):
        return globla_var.data

    def get_expect(self):
        return globla_var.expect

    def get_result(self):
        return globla_var.result
