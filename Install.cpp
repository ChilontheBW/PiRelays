#include <cstdlib>
#include <fstream>
#include <iostream>

using namespace std;
 
int main(){
	try{
		// downloads the newest versions of the relay controllers and program
		std::system("wget -O /home/pi/Downloads/relays https://github.com/ChilontheBW/PiRelays/archive/master.zip > /dev/null");
		
		// creates the new directory if needed
		bool cont = false;
		
		try{
			std::system("sudo mkdir /home/pi/python/Relays > /dev/null");
			cont = true;
	
		}catch (const std::exception &e){
		}

		if(cont){
			int inputsize = 15;
			std::string cmds[inputsize] = {
				"sudo unzip /home/pi/Downloads/relays -d /home/pi/python/Relays > /dev/null",
				"sudo rm -r /home/pi/Downloads/relays > /dev/null",
				"sudo mv /home/pi/python/Relays/PiRelays-master/bin /home/pi/python/Relays > /dev/null",
				"sudo mv /home/pi/python/Relays/PiRelays-master/src /home/pi/python/Relays > /dev/null",
				"sudo mv /home/pi/python/Relays/PiRelays-master/emergencymanager.desktop /home/pi/Desktop > /dev/null",
				"sudo mv /home/pi/python/Relays/PiRelays-master/README.md /home/pi/python/Relays > /dev/null",
				"sudo mv /home/pi/python/Relays/PiRelays-master/config.ini /home/pi/python/Relays > /dev/null",
				"sudo g++ /home/pi/python/Relays/PiRelays-master/RelayManager.cpp -o /home/pi/python/Relays/src/emergencymanager > /dev/null",				
				"sudo mv /home/pi/python/Relays/PiRelays-master/tightvncserver.service /etc/systemd/system/ > /dev/null",
				"sudo rm -r /home/pi/python/Relays/PiRelays-master > /dev/null",
				"sudo apt-get install tightvncserver -y> /dev/null",
				"sudo apt-get install xrdp -y> /dev/null",
				"sudo chown root:root /etc/systemd/system/tightvncserver.service > /dev/null",
				"sudo chown root:root ~/Desktop/emergencymanager.desktop > /dev/null",
				"sudo chmod +x ~/Desktop/emergencymanager.desktop > /dev/null",
				"sudo systemctl enable tightvncserver.service > /dev/null"};


			for(int i = 0; i < inputsize; i++){	
				try{
				std::system(cmds[i].c_str());
								
			}	
			std::string i = 0;
			cin >> i;
			std::exit(0);	
 		}
		else{
			std::exit(0);
		}
	}
	catch(const std::exception &e){
		std::cout << "Erorr in setup" << e.what() << std::endl;
		std::exit(1);
	}
}
