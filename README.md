# Local IoT setup using Python and Mosquitto

### Step 1: Set up a mosquitto broker 

Reference: https://www.vultr.com/docs/how-to-install-mosquitto-mqtt-broker-server-on-ubuntu-16-04


### Step 2: Use subsribe.py to subscribe to a topic to track any messages received on the broker for that particular topic

### Step 3: Use publish.py on any device connected to the LAN to publish messages to the broker.


Reference to python package: https://pypi.org/project/paho-mqtt/#simple

## Mosquitto commands

How to start a mosquitto server?

	mosquitto -v

How to kill a mosquitto server?

	ps -ef | grep mosquitto

	It lists all the processes 

	sudo kill <PID of the process>

How to subscribe to a topic?

	mosquitto_sub -h <host IP> -p <1883> -t “<topic name>”

How to publish to a topic from difference device on the LAN?

	mosquitto_pub -h <IPv4 address of the PC> -p <port of mosquitto server> -m “<message>” -t “<topic>”
