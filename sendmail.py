__author__ = 'Jan Philipp Harries'
#small utility to send mails from Gmail
#needs change to work for non-Gmail adresses

from email.mime.text import MIMEText
import smtplib
import time

def send_mail(from_adress, from_password, to_adress, text, subject, verbose=False):
    """
    from_adress - Email to send from - only gmail works currently
    from_password - account password
    to_adress - list/tuple of emails to send message to
    text - text of email
    subject - subject line of email
    """
    nachricht=text
    datum=time.strftime("%d.%m.%Y", time.localtime())
    msg = MIMEText(nachricht)
    msg["Subject"]=subject+" "+datum
    msg["From"]=from_adress
    msg["To"]=','.join(to_adress)
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.set_debuglevel(0)
    server.ehlo()
    server.starttls()
    server.login(from_adress,from_password)
    server.sendmail(from_adress,to_adress,msg.as_string())
    server.quit()
    if verbose:
        print "Statusmail gesendet"