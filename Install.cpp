#include <cstdlib>
#include <fstream>
#include <iostream>
 
int main(){
	try{
		// downloads the newest versions of the relay controllers and program
		std::system("wget -O /home/pi/Downloads/relays https://github.com/ChilontheBW/PiRelays/archive/master.zip");
		
		// creates the new directory if needed
		try{
		std::system("sudo mkdir /home/pi/python/relays");
		}catch (const std::exception &e){}
 
		// unpacks the new directory
		std::system("sudo unzip /home/pi/Downloads/relays -d /home/pi/python/relays");
		std::system("sudo rm -r /home/pi/Downloads/PiRelays-master");	
		
		// moves all needed program files and compiles the programmer
		std::system("sudo mv /home/pi/python/relays/PiRelays-master/bin /home/pi/Downloads/relays");
		std::system('sudo mv /home/pi/python/relays/PiRelays-master/"READ ME".text /home/pi/Downloads/relays');
		std::system("sudo mv /home/pi/python/relays/PiRelays-master/config.ini /home/pi/Downloads/relays");
		std::system("sudo g++ /home/pi/python/relays/PiRelays-master/RelayManager.cpp -o /home/pi/python/relays/emergencymanager");
		// moves the vnc startup config file 
		std::system("mv /home/pi/python/relays/PiRelays-master/tightvncserver.service /etc/systemd/system/");
		
		// installs the supporting programs
		std::system("sudo apt-get install tightvncserver");
		std::system("sudo apt-get install xrdp"); 

		// gives the vnc start files permissions and adds it to the startup files		
		std::system("sudo chown root:root /etc/systemd/system/tightvncserver.service");
		std::system("sudo chmod 755 /etc/systemd/system/tightvncserver.service");
		std::system("sudo systemctl enable tightvncserver.service");

		// removes all extra stuff	
		std::system("sudo rm -r /home/pi/python/relays/PiRelays-master");	
	}
	catch(const std::exception &e){
		std::cout << "Erorr in setup" << e.what() << std::endl;
	}
}
