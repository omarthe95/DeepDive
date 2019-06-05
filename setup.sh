mkdir output

String1="Host *"
String2="    StrictHostKeyChecking no"
String3="    KexAlgorithms=+diffie-hellman-group1-sha1"

file="/root/.ssh/config"
if grep -qF "$String1" "$file";then
   :
else
   echo "$String1" >> "$file"
fi

if grep -qF "$String2" "$file";then
   :
else
   echo "$String2" >> "$file"
fi

if grep -qF "$String3" "$file";then
   :
else
   echo "$String3" >> "$file"
fi

sudo apt update
sudo apt install python3-pip
pip3 --version
pip3 install netmiko
pip3 install netdev
pip3 install termcolor
pip3 install PrettyTable

