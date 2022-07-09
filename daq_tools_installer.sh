#!/bin/bash
sudo -v
sudo apt -y install spice-vdagent
sudo -v
sudo apt -y install gedit
sudo -v
sudo apt -y install python-is-python3
sudo -v
sudo apt -y install python3-pip
sudo -v
sudo apt -y install build-essential
sudo -v
sudo apt -y install libusb-1.0-0-dev
sudo -v
sudo apt -y install git-core
sudo -v
sudo apt -y install ipython3

mkdir -p ~/rawData/tempLog

mkdir -p ~/github
cd ~/github
git clone https://github.com/labjack/exodriver.git
sudo -v
cd ./exodriver
sudo ./install.sh
sudo -v
cd ~/github
git clone https://github.com/labjack/LabJackPython.git
sudo -v
cd ./LabJackPython
pip3 install setuptools
sudo -v
sudo python setup.py install
sudo -v
# labjack stuff is installed
wget -O - https://labs.picotech.com/Release.gpg.key | sudo apt-key add -
sudo bash -c 'echo "deb https://labs.picotech.com/rc/picoscope7/debian/ picoscope main" >/etc/apt/sources.list.d/picoscope7.list'
sudo -v
sudo apt-get update
sudo apt-get -y install picoscope
sudo -v
cd ~/github
git clone https://github.com/picotech/picosdk-python-wrappers.git
sudo -v
cd ./picosdk-python-wrappers
sudo python setup.py install
# picoscope stuff is installed
sudo -v
pip3 install numpy
sudo -v
pip3 install matplotlib
sudo -v
pip3 install pandas
sudo -v
pip3 install scipy

# install paraview
sudo apt install -y paraview

