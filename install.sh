#!/bin/bash
sudo apt-get install python3 -y
mkdir /opt/gods-eye
mv * /opt/gods-eye

rm -r "../Gods-eye"
pip3 install -r /opt/gods-eye/requirements.txt
ln /opt/gods-eye/gods-eye /bin/
chmod +x /usr/bin/gods-eye
echo "\nNOW YOU CAN ENTER gods-eye IN ANY TERMINAL TO OPEN gods-eye"
