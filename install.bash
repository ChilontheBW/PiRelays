filepath=/home/pi/python/relays

sudo apt-get update
sudo apt-get install -y rsync

#ufw
sudo apt-get install -y ufw
sudo ufw logging on
sudo ufw enable
sudo ufw allow ssh from 192.168.86.32/24

#ldap
sudo apt-get install -y libpam-ldapd libnss-ldapd

sudo rsync -Pavz --delete --rsync-path="sudo rsync"  KUOWhub:/mnt/relays "$(filepath)

#update scheduling
sudo systemctl enable --now atd.service
sudo apt-get install -y at
sudo at midnight + 7 days -f bash "$(filepath)/src/update.bash"
