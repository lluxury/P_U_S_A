#!/usr/bin/env python

import imaplib

username = 'third@huanlvjinfu.com.cn'
password = 'huanLV1128'

mail_server = 'mail.huanlvjinfu.com.cn'

i = imaplib.IMAP4_SSL(mail_server)
print i.login(username, password)
print i.select('INBOX')
for msg_id in  i.search(None, 'ALL')[1][0].split():
    print (msg_id)
    outf = open('%s.eml' % msg_id, 'w')
    outf.write(i.fetch(msg_id, '(RFC822)')[1][0][1])
    outf.close()
i.logout()
