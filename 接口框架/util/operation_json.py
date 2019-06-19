# coding:utf-8
import json


class OperationJson:

    def __init__(self):
        self.data = self.read_json_data()

    # 读取json文件
    def read_json_data(self):
        with open('../dataconfig/user.json') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_json_data(self, id):
        return self.data[id]


if __name__ == '__main__':
    opers = OperationJson()
    print(opers.get_json_data('user1'))
