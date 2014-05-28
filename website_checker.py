__author__ = 'Jan Philipp Harries'
"""
Simple tool to check if a given website has changed.
Just replace website, match_word, match_count check_intervall,
from_adress, from_password and to_adress and run.
"""

import datetime as dt
import urllib2
import re
from sendmail import send_mail
import time

website="www.test.de"
match_word='test'
match_count=1
check_intervall=dt.timedelta(hours=6)
from_adress="example@gmail.com"
from_password="123456"
to_adress=["example2@gmail.com"]


text="Website {} changed, match word {} not found {} times".format(website,match_word,match_count)
subject="Alert: Website {} changed".format(website)

start=dt.datetime.today()+dt.timedelta(seconds=3)
alerts=0

while True:
    now=dt.datetime.today()
    if now>=start:
        try:
            response = urllib2.urlopen('http://'+website)
            html = response.read()
            if len(re.findall(match_word,html))!=match_count:
                print "Website changed!"
                print dt.datetime.today()
                send_mail(from_adress,from_password,to_adress,text,subject,True)
                alerts+=1
            else:
                print "Nothing changed..."
                print dt.datetime.today()
        except urllib2.URLError:
            print "Website not available"
            subject="Alert: Website {} not available".format(website)
            send_mail(from_adress,from_password,to_adress,text,subject,True)
            alerts+=1
        start=now+check_intervall
        if alerts>=5:
            break
    time.sleep(1)
