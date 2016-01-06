#/usr/bin/python3
# Authored by Dawid Botha
# Released under no license. Modify, Sell, Whatever.
#YOLO #MyDayWear #DankMemes
from time import sleep
import requests
import datetime
import sendmail
import sys

f = open('pingdom2.log', 'a')
f.write ("###  startup: "+str(datetime.datetime.now())+"   ###\n")
f.flush()

timeout = 20
mailFrom="example@example.com"
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
    if not wasUpOnLastTest:
        if stringToCheckFor not in getpage(url):
            f.write ("\t"+str(datetime.datetime.now())+": site is still down :(\n")
        else:
            #site seems to be back
            f.write ("\t"+str(datetime.datetime.now())+": yay site is back up! Blasting the Masses with my email!\n")

            sendmail.sendmail(mailFrom,
                url + " is up",
                "Your webiste, "+url+" is back up!\nThis is the first check that succeeded after "+str(lastDowntime),
                recipients)
            wasUpOnLastTest=True
    else:
        if stringToCheckFor not in getpage(url):
            f.write (str(datetime.datetime.now())+": page is down, double checking\n")
            f.flush()
            #The DoubleCheck™
            sleep (15)
            if stringToCheckFor not in getpage(url):
                f.write ("\t"+str(datetime.datetime.now())+": okay site is definitely down!\n")
                sendmail.sendmail(mailFrom,
                        url + " is down",
                        "Your webiste, "+url+" is down!\nThis is the first downtime since "+str(lastDowntime),
                        recipients)
                wasUpOnLastTest = False
                lastDowntime = datetime.datetime.now()
            else:
                f.write ("\tOkay false alarm!\n")

    f.flush()
    sleep(35)
