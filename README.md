# Deep Dive into Cisco Network Programability
Inspired by Netmiko & Netdev to make scripts run much faster


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites:

* Linux OS (Recommended for Ubuntu 18.04)
* Python >=3.5 (pre-installed)
```
python --version
```

     
* SSH enabled and tested (connectivity)
```
ssh cisco@192.168.1.10
```

     
     
### Installing:

* Download the repository into a directory
```
git clone https://github.com/omarthe95/DeepDive.git
```

* Run setup.sh
```
bash setup.sh
```

* Edit **IPaddress_Switches.txt** file with your own IP address, each device IP per line
```
nano IPaddress_Switches.txt
```
* You may change the access credentials inside each python script individually, because the default access credentials into network devices is **cisco:Cisco123**




## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system


## Authors

* **Omar Adil** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Kirk Byers  
Python for Network Engineers  
https://pynet.twb-tech.com  


Sergey Yakovlev
Netdev
https://github.com/selfuryon/netdev
