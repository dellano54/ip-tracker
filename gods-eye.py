import requests
import webbrowser
import re
import sys


#command line arguments
if len(sys.argv) <= 1:
    print("NOT ENOUGH ARGUMENTS\nCorrect Usage: python gods_eye.py <ip_address> (or) gods_eye <ip_address>")
    sys.exit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("Correct Usage: python gods_eye.py <ip_address> (or) gods_eye <ip_address>")
    print("python gods_eye.py -h (or) --help => this message")
    sys.exit()

#intilizing variables

URL_API = "http://ip-api.com/json/"
MAP_ADDR = "https://www.google.com/maps/search/{lat},{lon}/data=!3m1!1e3?hl=en"
REGEX = re.compile(
    r'^('
    r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'  # 0-255
    r'\.){3}'
    r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'  # 0-255
    r'$'
)



#To check if its a valid ip address
def check(ip_addr: str):
    if not re.search(REGEX, ip_addr):
        print("ip address is not valid")
        sys.exit()


#check for ip location

def get_information(ip_addr: str):
    response = requests.get(URL_API+ip_addr)

    if response.status_code != 200:
        print("cant fetch details")
        sys.exit()

    data = response.json()
    lat, lon = data['lat'], data['lon']

    if data['status'] != "success":
        print("cant locate")
        sys.exit()

    print(" IP: ", data['query'])
    print(" Status: ", data['status'])
    print(" city: ", data['city'])
    print(" ISP: ", data['isp'])
    print(" latitude: ",  lat)
    print(" longitude: ", lon)
    print(" country: ", data['country'])
    print(" region: ", data['regionName'])
    print(" city: ", data['city'])
    print(" zip: ", data['zip'])
    print(" AS: ", data['as'])


    webbrowser.open(
        MAP_ADDR.format(
            lat=lat,
            lon=lon
        )
    )
    

ip_addr = sys.argv[1]
check(ip_addr)
get_information(ip_addr)
