# coding:utf-8
import json


class OperationJson:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../dataconfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_json_file()

    # 读取json文件
    def read_json_file(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_json_data(self, id=None):
        if (id == None):
            return None
        else:
            return self.data[id]

    # 将cookie写进json文件
    def write_data(self, data):
        with open('../dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    opers = OperationJson()
    print(opers.get_json_data())
