sudo apt-get update

wget -O /home/pi/Downloads/relays https://github.com/ChilontheBW/PiRelays/archive/master.zip

sudo mkdir -p /home/pi/python/Relays

#python relays, to be shortened with rsync
sudo unzip /home/pi/Downloads/relays -d /home/pi/python/Relays
sudo rm -r /home/pi/Downloads/relays
sudo mv /home/pi/python/Relays/PiRelays-master/bin /home/pi/python/Relays
sudo mv /home/pi/python/Relays/PiRelays-master/src /home/pi/python/Relays
sudo mv /home/pi/python/Relays/PiRelays-master/emergencymanager.desktop /home/pi/Desktop
sudo mv /home/pi/python/Relays/PiRelays-master/README.md /home/pi/python/Relays
sudo mv /home/pi/python/Relays/PiRelays-master/config.ini /home/pi/python/Relays
sudo g++ /home/pi/python/Relays/PiRelays-master/RelayManager.cpp -o /home/pi/python/Relays/src/emergencymanager
sudo mv /home/pi/python/Relays/PiRelays-master/tightvncserver.service /etc/systemd/system/
sudo rm -r /home/pi/python/Relays/PiRelays-master
sudo apt-get install tightvncserver -y
sudo apt-get install xrdp -y
sudo chown root:root /etc/systemd/system/tightvncserver.service
sudo chown root:root ~/Desktop/emergencymanager.desktop
sudo chmod +x ~/Desktop/emergencymanager.desktop
sudo systemctl enable tightvncserver.service


#update scheduling
sudo apt-get install -y at

#ldap
sudo apt-get install -y libpam-ldapd libnss-ldapd


#ufw
sudo apt-get install -y ufw
sudo ufw logging on
sudo ufw enable
sudo ufw allow ssh
