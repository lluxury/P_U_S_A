#!/usr/bin/env python

import smtplib
mail_server = 'localhost'
mail_server_port = 25

from_addr = 'sender@example.com'
to_addr = 'receiver@example.com'

from_header = 'From: %s\r\n' % from_addr
to_header = 'To: %s\r\n\r\n' % to_addr
subject_header = 'Subject: nothing interesting'

body = 'This is a not-very-interesting email.'

email_message = '%s\n%s\n%s\n\n%s' % (from_header, to_header, subject_header, body)

s = smtplib.SMTP(mail_server, mail_server_port)
s.sendmail(from_addr, to_addr, email_message)
s.quit()


#定义主机和端口, to和from,连接邮件头与邮件体
# 4个参数代入函数
#连接smtp服务器 域名,端口 ,代入3个参数发邮件
#结束

#没有验证成功与否