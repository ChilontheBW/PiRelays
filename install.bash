filepath=/home/pi

sudo apt-get update
sudo apt-get install -y rsync

#ufw
sudo apt-get install -y ufw
sudo ufw logging on
sudo ufw enable
sudo ufw allow ssh

#ldap
sudo rsync -Pavz --delete --rsync-path="sudo rsync"  KUOWhub:/mnt/pi "$(filepath)"

#update scheduling
sudo systemctl enable --now atd.service
sudo apt-get install -y at
sudo at midnight + 7 days -f bash "$(filepath)/src/update.bash"
