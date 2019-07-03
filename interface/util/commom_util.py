#coding:utf-8
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