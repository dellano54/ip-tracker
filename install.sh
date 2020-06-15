#!/bin/bash
sudo apt-get install python3 alsa-utils figlet espeak -y
mkdir /opt/gods-eye
mv * /opt/gods-eye
cd ..
rm -r Gods-eye
cd /opt/gods-eye/
pip3 install -r requirements.txt
ln gods-eye /bin/
chmod +x /usr/bin/gods-eye
echo "
"
echo "NOW YOU CAN ENTER gods-eye IN ANY TERMINAL TO OPEN gods-eye"
