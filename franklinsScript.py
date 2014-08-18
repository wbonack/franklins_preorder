import time
import datetime
from bs4 import BeautifulSoup
from urllib2 import urlopen
import html2text
from twilio.rest import TwilioRestClient 

BASE_URL = "https://franklinbarbecue.com/preorders"

print "Hey there"

def getText():
     html = urlopen(BASE_URL).read()
     soup = BeautifulSoup(html, "lxml")
     text = soup.find("div","main")

     txt = text.get_text().encode('utf-8')
     return txt

txt = getText()

f = open("text.txt","r")
file_txt = f.read()
#file_txt = txt
#f.write(txt)
#'''
while True:
    log = open("log.txt","w")
    
    if txt == file_txt:
        message = "They are equal " + str(datetime.datetime.now().time())
	print message
	log.write(message)
	
	
    else:
        message =  "They are different " + str(datetime.datetime.now().time())
	print message
    log.close()

    txt = getText()

    time.sleep(300)
#'''
