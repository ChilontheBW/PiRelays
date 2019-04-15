filepath=/home/pi

sudo apt-get update

#ufw
sudo apt-get install -y ufw
sudo ufw logging on
sudo ufw enable
sudo ufw allow ssh

#update scheduling
sudo systemctl enable --now atd.service
sudo apt-get install -y at
sudo at midnight + 7 days -f bash "$(filepath)/src/update.bash"
