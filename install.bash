filepath=/home/pi

sudo apt-get update

sudo apt-get install -y vim
sudo apt-get install -y screen



#keygen and sync
mkdir -p /home/pi/.ssh
ssh-keygen -t rsa -b 4096 -v -f /home/pi/.ssh/sshkeygen -N ""
chmod 600 .ssh/sshkeygen.pub
ssh-copy-id -i /home/pi/.ssh/sshkeygen.pub pi@10.144.81.4

ip="$(ip addr | grep 'global eth0' | grep -o '[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*' | grep -v '255')"

ip_file="$(ssh 10.144.81.4 -T "less /home/pi/alert/src/config.ini" | grep -E '(ip_.*=).*' | grep -o '[^=]*$')"

nameNum="$(ssh 10.144.81.4 -T "less $ip_file |  wc -l")"
cat "kuowalert$nameNum" > /etc/hostname
s
echo "$ip:kuowalert$nameNum" | ssh 10.144.81.4 -T "cat >> $ip_file"
sudo usermod --password KUOWraspbpi94.9 pi


rsync -Pavz --delete --rsync-path="sudo rsync" 10.144.81.4:/home/pi/alert /home/pi

rsync -Pavz --rsync-path="sudo rsync" --exclude 'sshkeygen*' 10.144.81.4:/home/pi/.ssh home/pi


#ufw
sudo apt-get install -y ufw
sudo ufw logging on
sudo ufw enable
sudo ufw allow ssh
	

#update scheduling
sudo apt-get install -y at
sudo systemctl enable --now atd.service
sudo at midnight + 7 days -f bash "$(filepath)/src/update.bash"



sudo shutdown -r 0

