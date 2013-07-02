# coding=gbk
import sys
reload(sys)
import smtplib
sys.setdefaultencoding('utf-8')
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
#############
mailto_list=["18359255605@139.com"]
#####################
mail_host="smtp.163.com"
mail_user="xqiugen"
mail_pass="123456789.0"
mail_postfix="163.com"
#print mail_host
#print mail_user
#print mail_pass
#print mail_postfix
######################
def send_mail(to_list,sub,content):
    print "this is send mail"
    print sub,content
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    # point out the encoding of mail
    #or chinese character will be gibberish
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    print "start"
    if send_mail(mailto_list,"subject","content"):
        print "true"
    else:
        print "fail"
