import smtplib

text = 'This is a testmail'
fromaddr = 'you@ins.hsr.ch'
toaddr = 'someone@ins.hsr.ch'

# 'To' and 'From' addresses must be included in the message headers explicitly
msg = 'From: {f}\r\nTo: {t}\r\n\r\n{text}'.format(f=fromaddr, t=toaddr, text=text)

server = smtplib.SMTP('mail.ins.hsr.ch')
# server.login(user, password)
server.sendmail(fromaddr, toaddr, msg)
