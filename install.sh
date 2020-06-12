#!/bin/bash
sudo apt-get install python3 alsa-utils -y
mkdir /opt/ip-tracker
mv * /opt/ip-tracker
cd /opt/ip-tracker/
pip3 install -r requirements.txt
ln tracker /bin/
echo "
"
echo "NOW YOU CAN ENTER tracker IN ANY TERMINAL TO OPEN IP-TRACKER"
