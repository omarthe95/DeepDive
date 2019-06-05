#!/usr/bin/python3

import threading, os, time, sys ,socket
from multiprocessing import Queue
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

start = time.time()

# Define username and password to login to all routers with
USER = 'cisco'
PASSWORD = 'Cisco123'

# Define Switches IPs
#Switches = ['10.200.200.10', '10.200.200.11', '10.200.200.12', '10.200.200.13', '10.200.200.14', '10.200.200.15','10.200.200.16', '10.200.200.17']
# Switches = ['10.200.200.16']
Switches=[]

with open('IPaddress_Switches.txt') as f:
    for line in f:
        line = line.strip()
        try:
            socket.inet_aton(line)
            Switches.append(line)

        except socket.error:
            print ("Invalid IP address  " + line)

print ("This is Switches IPs: \n")
print (Switches)
print("\n")

os.chdir("output/")


def ssh_session(switch, output_q):
    # Place what you want each thread to do here, for example connect to SSH, run a command, get output
    output_dict = {}
    switch_d = {'device_type': 'cisco_ios', 'ip': switch, 'username': USER, 'password': PASSWORD}

    # SSH Iteration
    try:
        ssh_session = ConnectHandler(**switch_d)
    except (AuthenticationException):
        print("Wrong Authentication >>> "+ (switch_d['ip']) + "\n")
        pass
    except (NetMikoTimeoutException):
        print("Timeout >>> "+ (switch_d['ip']) + "\n")
        pass
    except (EOFError):
        print("EOF Error >>> "+ (switch_d['ip']) + "\n")
        pass
    except (SSHException):
        print("Error SSH Exception >>> "+ (switch_d['ip']) + "\n")
        pass
    except Exception as unknown_error:
        print("Unkown Error >>> "+ (switch_d['ip']) + "\n")
        pass

    else:

        # Get the device Hostname
        hostname = ssh_session.send_command('show run | inc host')
        hostname = hostname[9:]
        hostname.split(" ")
    
        # Put the Output into a Dictionary to use it later with threading Queue
        output = ssh_session.send_command("show run ")
        output_dict[hostname] = output
        output_q.put(output_dict)
  
        # Save the output into a file with Device Hostname
        f = open((hostname), "w")
        print((output), file=f)  # python 3.x

        # print >>f, (output)  #python 2.x



if __name__ == "__main__":

    output_q = Queue()

    # Start thread for each switch in Switches list
    for switch in Switches:
        my_thread = threading.Thread(target=ssh_session, args=(switch, output_q))
        my_thread.start()

    my_thread.join()




end = time.time()
total = int(end - start)
print("\n Elapsd Time: " + str(total) + " Sec\n")

sys.exit(1)