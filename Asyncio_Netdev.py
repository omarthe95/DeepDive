#!/usr/bin/python3

import asyncio
import netdev
import os, time, sys ,socket, json

USER = 'cisco'
PASSWORD = 'Cisco123'

start = time.time()

# Define username and password to login to all routers with

Switches_dic=[]
Switches_IP=[]



with open('IPaddress_Switches.txt') as f:
    for line in f:
        line = line.strip()
        try:
            socket.inet_aton(line)
            Switches_IP.append(line)
            IP = { 'username' : USER,'password' : PASSWORD,'device_type': 'cisco_ios','host': line}
            Switches_dic.append(IP)

        except socket.error:
            print ("Invalid IP address  " + line)

print ("This is Switches IPs: \n")
print (Switches_IP)
print("\n")

os.chdir("output/")

async def task(param):

    async with netdev.create(**param) as ios:
        # Get the device Hostname
        hostname = await ios.send_command("show run | inc hostname")
        hostname = hostname[9:]
        hostname.split(" ")
        print (hostname)

        output = await ios.send_command("show run")
 
        f = open((hostname), "w")
        print((output), file=f)  # python 3.x



async def run():

    
    tasks = [task(switch) for switch in Switches_dic]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())

end = time.time()
total = int(end - start)
print("\n Elapsd Time: " + str(total) + " Sec\n")

sys.exit(1)
