import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self, username, passwd, recv, title, content,
                 file=None, ssl=False,
                 email_host='smtp.qq.com', port=25, ssl_port=465):
        self.username = username  # 用户名
        self.passwd = passwd  # 密码
        self.recv = recv  # 收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = title  # 邮件标题
        self.content = content  # 邮件正文
        self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host  # smtp服务器地址
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全链接
        self.ssl_port = ssl_port  # 安全链接端口

    def send_email(self,pass_list,fail_list):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  # 处理附件的
            file_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        text="此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result )
        msg.attach(MIMEText(self.content+'\n'+text))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()
if __name__ == '__main__':
    m = SendEmail(
        username='2712894324@qq.com',
        passwd='liwuxgyhupzhdfgj',
        recv=['2712894324@qq.com'],
        title='555',
        content='接口自动化测试结果如下：',
        file=r'C:\Users\admin\Desktop\suites.csv',
        ssl=True,
    )
    m.send_email([1,2,3,4],[2,3,4,5,6,7])