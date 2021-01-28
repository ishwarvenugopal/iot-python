import argparse
import paho.mqtt.client as mqttClient
import time

Connected = False   #global variable for the state of the connection

def parse_arguments():
    parser = argparse.ArgumentParser(description= "Publishing MQTT signals to local server")
    parser.add_argument('-hn', "--host", required= True, help = "Hostname of the MQTT broker")
    parser.add_argument('-p',"--port", required= True, type = int, help = "Port to connect to the MQTT broker")
    parser.add_argument("-u","--user", required = True, help = "Username of the MQTT broker")
    parser.add_argument("-pw","--password", required = True, help = "Password for the MQTT broker")
    parser.add_argument("-t","--topic", required = True, help = "Topic to subscribe")
    return parser.parse_args()

# Callback function that checks if the connection was successful, 
# and updates the value of the boolean 'Connected'
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
 
def publish_signals(args):
    # Details regarding the MQTT brocker
    broker_address= args.host
    port = args.port
    user = args.user
    password = args.password

    # Setting up the client
    print("Creating client")
    client = mqttClient.Client("Test Device")               #create new instance
    client.username_pw_set(user, password=password)    #set username and password
    client.on_connect= on_connect                      #attach function to callback
    print("Connecting to Broker")
    client.connect(broker_address, port=port)          #connect to broker
    client.loop_start()        #start the loop
    while Connected != True:    #Wait for connection
        time.sleep(0.1)
    
    try:
        while True:
            value = input('Enter the message:')
            client.publish(args.topic,value)

    except KeyboardInterrupt:
        client.disconnect()
        client.loop_stop()

if __name__ == '__main__':
    args = parse_arguments()
    print("Arguments parsed")
    publish_signals(args)
    
