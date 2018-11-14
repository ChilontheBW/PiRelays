#include <cstdlib>
#include <fstream>
#include <iostream>

using namespace std;
 
int main(){
	try{
		// downloads the newest versions of the relay controllers and program
		std::system("wget -O /home/pi/Downloads/relays https://github.com/ChilontheBW/PiRelays/archive/master.zip");
		
		// creates the new directory if needed
		bool cont = false;
		
		try{
			std::system("sudo mkdir /home/pi/python/relays");
			cont = true;
	
		}catch (const std::exception &e){
			char* input = new char[20];
			std::cout << "Package already installed, do you want to continue install?";
			std::cin >> input;
	
			if(input[0] == char('y')){	
				cont = true;		
			}

		delete [] input;
		}

		

		if(cont){
			int inputsize = 13;
			std::string cmds[inputsize] = {"sudo unzip /home/pi/Downloads/relays -d /home/pi/python/relays",
				"sudo rm -r /home/pi/Downloads/PiRelays-master",
				"sudo mv /home/pi/python/relays/PiRelays-master/bin /home/pi/Downloads/relays",
				"sudo mv /home/pi/python/relays/PiRelays-master/'READ ME'.text /home/pi/Downloads/relays",
				"sudo mv /home/pi/python/relays/PiRelays-master/config.ini /home/pi/Downloads/relays",
				"sudo g++ /home/pi/python/relays/PiRelays-master/RelayManager.cpp -o /home/pi/python/relays/emergencymanager",
				"mv /home/pi/python/relays/PiRelays-master/tightvncserver.service /etc/systemd/system/",
				"sudo apt-get install tightvncserver",
				"sudo apt-get install xrdp",
				"sudo chown root:root /etc/systemd/system/tightvncserver.service",
				"sudo chmod 755 /etc/systemd/system/tightvncserver.service",
				"sudo systemctl enable tightvncserver.service",
				"sudo rm -r /home/pi/python/relays/PiRelays-master"
				}
			for(int i = 0; i< inputsize; i++){
			std::system(cmds[i]);
			}	
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
