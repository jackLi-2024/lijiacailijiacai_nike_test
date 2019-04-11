#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# """
# File:   .py
# Author: wld
# Date: 2019-xx-xx
# Description:
# """

from config import *
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header


class Email(object):
    '''
    注意：文件名需加上扩展名，查看邮箱时浏览器可解析显示
    '''

    # 初始化邮件相关配置
    def __init__(self):
        self.__smtpserver = email_smtpserver
        self.__smtport = email_port
        self.__sender = email_sender
        self.__password = email_password
        self.__receiver = email_receiver
        self.__subject = email_subject + "    " + \
                         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.__subject = Header(self.__subject, 'utf-8').encode()
        self.__msg = MIMEMultipart('mixed')
        self.__msg['Subject'] = self.__subject
        self.__msg['From'] = self.__sender
        self.__msg['To'] = ";".join(self.__receiver)

    # 附加文本内容
    def appendText(self, text):
        text_plain = MIMEText(text, 'plain', 'utf-8')
        self.__msg.attach(text_plain)

    # 附加图片 imgBytes:图片的二进制数据 imgName:图片名称
    def appendImage(self, imgBytes, imgName):
        image = MIMEImage(imgBytes)
        image.add_header('Content-Disposition', 'attachment', filename=imgName)
        self.__msg.attach(image)

    # 附加html htmlStr:字符串
    def appendHtml(self, htmlStr, htmlName):
        text_html = MIMEText(htmlStr, 'html', 'utf-8')
        text_html.add_header('Content-Disposition',
                             'attachment', filename=htmlName)
        self.__msg.attach(text_html)

    # 附加附件
    def appendAttachment(self, attachName):
        pass

    # 发送邮件
    def sendEmail(self):
        try:
            smtp = smtplib.SMTP_SSL(self.__smtpserver, self.__smtport)
            smtp.login(self.__sender, self.__password)
            smtp.sendmail(self.__sender, self.__receiver,
                          self.__msg.as_string())
            print("发送成功")
        except Exception as e:
            print(e)
            print("发送失败")
        finally:
            smtp.quit()

    def test(self):
        try:
            self.appendText("hello world!\n I am coming!")
            sendimagefile = open(r'./a.png', 'rb').read()
            self.appendImage(sendimagefile, "测试图片.png")
            html = """
                <html>  
                <head></head>  
                <body>  
                    <p>Hi!<br>  
                    How are you?<br>  
                    Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
                    </p> 
                </body>  
                </html>  
                """
            self.appendHtml(html, "测试页面.html")

            smtp = smtplib.SMTP_SSL(self.__smtpserver, self.__smtport)
            smtp.login(self.__sender, self.__password)
            smtp.sendmail(self.__sender, self.__receiver,
                          self.__msg.as_string())
            print("发送成功")
        except Exception as e:
            print(e)
            print("发送失败")
        finally:
            try:
                smtp.quit()
            except:
                pass


if __name__ == "__main__":
    email = Email()
    email.test()
