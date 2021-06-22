# Internship-SW_IoT
Spot Welding IoT Device Development



Project Objective: 

To introduce an IoT feature to display all the contents required for Spot Welding Cell. The IoT feature can be achieved by using a Raspberry Pi which sends the accumulated data via router/internet access. 

The main objective is to retrieve data from all the components and display it in the client's device. 





Project Components : 

OMRON PLC - CJ2M-CPU33

Fanuc controller - R-30iB
Nadesco AC controller - PH5S-1000-N1EJ-L0P0-14020
Raspberry Pi
Router 





Communication between Raspberry Pi and CJ2M :

~ We first allocated an IP-Address to CJ2M using the CX-one software. Along with the IP address we also required the UDP port number.

~ After connecting the PLC to a Switch, we check the IP address using IP Tracker. 

~ Since our goal was to communicate using Ethernet Port, After several researches done we were able to use FINS/UDP protocol. [ MODBUS communication is not advised for the project since we cant add a new function block ]

~FINS( Factory Intelligent Network Services) is widely used in automation factories; due to its open source programs we were able to find a script that works in python.

~ The python script requires the PLC’s IP address and the UDP port number. 

~ After running the python program, we ran a loop program to understand how many memory sites can be accessed. 

~A0-A999; C0-C999; D0-D999; around 3000 memory sites can be accessed using FINS. (didn't use any function blocks)

~ Our goal was achieved; since we just need to access the memory site and display the data accordingly. 







Communication between Raspberry Pi and Fanuc controller - R-30iB :

~ We first manually set the IP-Address using the Ipendant. After connecting the Fanuc controller to the laptop via ethernet, we used an IP tracker. 

~ In case of fanuc controller, the data is accessed with following parameters Class , Instance and Attribute. 

~ While executing the script make sure you address the particular parameter . 

