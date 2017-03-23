import smtplib  
import email.mime.multipart  
import email.mime.text  
  
msg=email.mime.multipart.MIMEMultipart()  
msg['from']='ustchacker@tom.com'  
msg['to']='blablabla@aliyun.com'  
msg['subject']='test'  
content=''''' 
abc:
    def
        gh
'''  
txt=email.mime.text.MIMEText(content)  
msg.attach(txt)  
  
smtp=smtplib  
smtp=smtplib.SMTP()  
smtp.connect('smtp.tom.com','25')  
smtp.login('ustchacker@tom.com','password')  
smtp.sendmail('ustchacker@tom.com','blablabla@aliyun.com',str(msg))  
smtp.quit() 