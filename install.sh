#!/bin/bash
sudo apt-get install python3 alsa-utils figlet -y
mkdir /opt/ip-tracker
mv * /opt/ip-tracker
cd ..
rm -r Gods-eye
cd /opt/ip-tracker/
pip3 install -r requirements.txt
ln godseye /bin/
echo "
"
echo "NOW YOU CAN ENTER godseye IN ANY TERMINAL TO OPEN IP-TRACKER"
