import urllib
from urllib.request import urlopen as open
import os
import json
import pyttsx3
import re 
import webbrowser



os.system ("figlet G O D S - E Y E")
print("                                       -by dellano samuel fernandez")
engine = pyttsx3.init('espeak')





def goto2():
    global ip
    ip = input("Enter ip address  : ")
    url = "http://ip-api.com/json/"
    check(ip)



    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
    
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

       
def check(Ip):  
    if(re.search(regex, Ip)):  
        print("Valid Ip address found")
        speak("locating sir")
        goto1()

     
    else:
        print("Invalid ip address")
        speak("Invalid ip address,sir")
        goto2()

def goto1():
   
    url = "http://ip-api.com/json/"
    response = open(url + ip)
    data = response.read()
    values = json.loads(data)
    status = values['status']
    success = "success"
    lat = str(values['lat'])
    lon = str(values['lon'])
    a = lat + ","
    b = lon + "/"
    c = b + "data=!3m1!1e3?hl=en"
    location = a + c


    maps = "https://www.google.com/maps/search/"
    webbrowser.open(maps + location)
    

    print(" IP: " + values['query'])
    print(" Status: " + values['status'])
    print(" city: " + values['city'])
    print(" ISP: " + values['isp'])
    print(" latitude: " + lat)
    print(" longitude: " + lon)
    print(" country: " + values['country'])
    print(" region: " + values['regionName'])
    print(" city: " + values['city'])
    print(" zip: " + values['zip'])
    print(" AS: " + values['as'])
    if status == success:
        speak("sucessfully located")
    else:
        speak("cannot find the location,sir")    
    
    goto2()           
        
goto2()
            
