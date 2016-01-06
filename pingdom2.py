#/usr/bin/python3
# Authored by Dawid Botha
# Released under no license. Modify, Sell, Whatever.
#YOLO #MyDayWear #DankMemes
from time import sleep
import requests
import datetime
import sendmail
import sys

timeout = 20
mailFrom="example@production.server.com"
recipients = ["example@example.com"]
url=sys.argv[1]
stringToCheckFor=sys.argv[2]

def getpage(url):
    try:
        data=requests.get(url, timeout=timeout).text
        return data
    except Exception as inst:
        return "idec what went wrong lol"

lastDowntime = 'never'
wasUpOnLastTest=True
while True:
    if stringToCheckFor not in getpage(url):
        print ("page is down, double checking")
        #The DoubleCheck™
        if stringToCheckFor not in getpage(url):
            print ("okay site is definitely down!")
            if wasUpOnLastTest:
                print ("Just went down, emailing everyone")
                sendmail.sendmail(mailFrom,
                        url + " is down",
                        "Your webiste, "+url+" is down!\nThis is the first downtime since "+str(lastDowntime),
                        recipients)
                wasUpOnLastTest = False
                lastDowntime = datetime.datetime.now()
            print ("site is still down :(")

    else:
        if not wasUpOnLastTest:
            print ("yay site is back up! Blasting the Masses with my email!")

            sendmail.sendmail(mailFrom,
                    url + " is up",
                    "Your webiste, "+url+" is back up!\nThis is the first check that succeeded after "+str(lastDowntime),
                    recipients)

            wasUpOnLastTest=True

        else:
            print ("all is still fine at "+str(datetime.datetime.now()))
    sleep(15)
