# Local IoT setup using Python and Mosquitto

### Step 1: Set up a mosquitto broker 

Reference: https://www.vultr.com/docs/how-to-install-mosquitto-mqtt-broker-server-on-ubuntu-16-04

Once mosquitto is installed and configured, start the mosquitto server

`mosquitto -v`

### Step 2: Subscribe to a topic

Using subscribe.py:

`python3 subscribe.py -hn <host IP address> -p <port number> -u <mosquitto username> -pw <mosquitto password> -t <topic>`

Using mosquitto commands:

`mosquitto_sub -h <host IP address> -p <port number> -t “<topic>”`

Once this is kept running, it keeps track of all message received by the broker on that topic.

### Step 3: Publishing to a topic (from same device or from different device on the LAN):

Using publish.py:

`python3 publish.py -hn <IPv4 address of the PC> -p <port number> -u <mosquitto username> -pw <mosquitto password> -t <topic>`

Using mosquitto commands:

`mosquitto_pub -h <IPv4 address of the PC> -p <port number> -m “<message>” -t “<topic>”`

### Stopping the mosquitto server

`ps -ef | grep mosquitto`

It lists all the processes 

`sudo kill <PID of the process>`


Reference to python package used: https://pypi.org/project/paho-mqtt/#simple
