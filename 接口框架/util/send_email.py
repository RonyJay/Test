# coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global mail_host
    global mail_user
    global mail_pass
    global to_receivers,cc_receivers
    mail_host = 'smtp.163.com'
    mail_user = 'meltest16@163.com'
    mail_pass = 'iobit2013'
    # 发送给自己，可以避免被当做垃圾邮件
    to_receivers = ['409169403@qq.com','meltest16@163.com']
    cc_receivers = ['meltest16@163.com']

    def send_email(self):
        try:
            msg = MIMEText(content, _subtype='plain', _charset='utf-8')
            msg['From'] = mail_user
            msg['To'] = ';'.join(to_receivers)
            msg['Cc']=';'.join(cc_receivers)
            msg['Subject'] = '接口测试报告'
            server = smtplib.SMTP(mail_host, 25)
            server.login(mail_user, mail_pass)
            server.sendmail(mail_user,msg['To']+msg['Cc'],msg.as_string())
            server.quit()
            print("邮件发送成功")
        except smtplib.SMTPException as n:
            print("Error:无法发送邮件")
            print(n)


if __name__ == '__main__':
    sen = SendEmail()
    content = '接口结果lalala'
    sen.send_email()
