#coding:utf-8
import json
import operator
class CommonUtil(object):
    def is_contain(self,str1,str2):
        '''
        判断一个字符串是否在另一个字符串中
        :param str1:查找的字符串
        :param str2: 被查找的字符串
        :return:
        '''
        flag=None
        if str1 in str2:
            flag=True
        else:
            flag=False
        return flag

    '''
    对比两个字典是否相同
    字典是无序的
    '''
    def is_equal_dict(self,dict1,dict2):
        if isinstance(dict1,str):
            dict1=json.loads(dict1)
        if isinstance(dict2,str):
            dict2=json.loads(dict2)
        return operator.eq(dict1,dict2)