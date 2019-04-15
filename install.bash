filepath=/home/pi

sudo apt-get update

#keygen and sync
sudo mkdir -p /home/pi/.ssh
sudo ssh-keygen -t rsa -b 4096 -v -f /home/pi/.ssh/sshkeygen -N ""
sudo rsync -Pavz --delete --rsync-path="sudo rsync" /home/pi/.ssh/sshkeygen.pub 


#ufw
sudo apt-get install -y ufw
sudo ufw logging on
sudo ufw enable
sudo ufw allow ssh


#update scheduling
sudo systemctl enable --now atd.service
sudo apt-get install -y at
sudo at midnight + 7 days -f bash "$(filepath)/src/update.bash"
