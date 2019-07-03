# coding:utf-8

class globla_var(object):
    # case_id
    id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    json_key = '9'
    expect = '10'
    result = '11'

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
        return globla_var.header
        # return self.get_header()

    def get_case_depend(self):
        return globla_var.case_depend

    def get_data_depend(self):
        return globla_var.data_depend

    def get_field_depend(self):
        return globla_var.field_depend

    def get_json_key(self):
        return globla_var.json_key

    def get_expect(self):
        return globla_var.expect

    def get_result(self):
        return globla_var.result
