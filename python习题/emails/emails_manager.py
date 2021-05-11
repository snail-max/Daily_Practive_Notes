# -*-coding:utf-8-*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import requests
import json


class EmailsManage():

    def emails(self):
        # 定义smtp的服务器是什么
        smtpserver = 'smtp.163.com'
        # 发送邮件的用户名和密码
        username = ''
        passwd = ''  # 授权密码
        # 接收的邮件的邮箱
        receiver = ['785161347@qq.com', '2398391057@qq.com']
        # 创建邮件的对象
        message = MIMEMultipart('related')
        # 设置邮件的标题
        subject = "上海扫黄打非办"  # 邮件的主题

        content_json = requests.get('https://api.xygeng.cn/one').json()
        if content_json['code'] == 200:
            content = content_json['data']['content']
        else:
            content = '未收到名言'

        '''获取金山词霸每日一句'''
        url = 'http://open.iciba.com/dsapi'
        r = requests.get(url)
        content_text = r.json()['content']
        note_text = r.json()['note']
        # 附件
        # fujian = MIMEText(open('report.html', 'rb').read(), 'html', 'utf-8')  # 附件
        content = content+'\t'\
                  +'\n'+content_text+\
                  '\n'+note_text
        content_text = MIMEText(content)

        # 把邮件的信息组装到邮件的对象
        message['from'] = username
        message['to'] = ";".join(receiver)  # 实现群发
        message['subject'] = subject
        # message.attach(fujian)
        message.attach(content_text)


        # 登录smtp服务器发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, passwd)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()


if __name__ == '__main__':
    c = EmailsManage()
    c.emails()
