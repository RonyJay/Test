# coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global mail_host
    global mail_user
    global mail_pass
    global to_receivers, cc_receivers
    mail_host = 'smtp.163.com'
    mail_user = 'meltest16@163.com'
    mail_pass = 'iobit2013'
    # 发送给自己，可以避免被邮件服务器拦截
    to_receivers = ['meltest16@163.com', '409169403@qq.com']
    cc_receivers = ['meltest16@163.com']

    def send_email(self,content):
        try:
            msg = MIMEText(content, _subtype='plain', _charset='utf-8')
            msg['From'] = mail_user
            msg['To'] = ';'.join(to_receivers)
            msg['Cc'] = ';'.join(cc_receivers)
            msg['Subject'] = '接口自动化测试报告'
            server = smtplib.SMTP(mail_host, 25)
            server.login(mail_user, mail_pass)
            server.sendmail(mail_user, msg['To'].split(';') + msg['Cc'].split(';'), msg.as_string())
            server.quit()
            print("邮件发送成功")
        except smtplib.SMTPException as n:
            print("Error:无法发送邮件")
            print(n)

    def send_main(self, pass_list, fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result="%.2f%%" % (fail_num / count_num * 100)
        content = "此次一共运行接口个数为%d个，通过个数为%d，失败个数为%d，通过率为%s,失败率为%s" % \
                  (count_num, pass_num, fail_num, pass_result,fail_result)
        self.send_email(content)

if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1,2,3,4],[5,6,7])
