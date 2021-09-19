from urllib.request import urlopen as open
import json
import pyttsx3
import re 
import webbrowser
from pyfiglet import Figlet


print(Figlet().renderText('Gods - eye'))
print("                                       -by dellano samuel fernandez")
engine = pyttsx3.init()





def goto2():
    global ip
    ip = input("Enter ip address  : ")
    exit() if ip.lower() == 'exit' else check(ip)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
    
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

       
def check(Ip):
    if(Ip.startswith('192')):
        print("I think its a private ip address")
        speak('Invalid ip address,sir')
        goto2()

    elif(re.search(regex, Ip)): 
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
    b = lon + "/" + "data=!3m1!1e3?hl=en"
    location = a + b


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
          
