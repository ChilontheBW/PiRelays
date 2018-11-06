#include <cstdlib>
#include <fstream>
#include <iostream>
 
int main()
{
std::system("wget -O /home/pi/python/relays https://github.com/ChilontheBW/PiRelays/archive/master.zip")

std::system("sudo apt-get install tightvncserver")
std::system("sudo apt-get install xrdp")

std::system("mv /home/pi/python/relays/tightvncserver.service /etc/systemd/system/")

std::system("sudo chown root:root /etc/systemd/system/tightvncserver.service")
std::system("sudo chmod 755 /etc/systemd/system/tightvncserver.service")
std::system("sudo systemctl enable tightvncserver.service")
}
