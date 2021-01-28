import paho.mqtt.subscribe as subscribe
import argparse 

def on_message_print(client, userdata, message):
    print("{}: {}".format(message.topic, str(message.payload)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Subscribing to MQTT signals')
    parser.add_argument("-hn","--host", required = True, help = "Hostname of the MQTT broker")
    parser.add_argument("-p","--port", required = True, type = int, help = "Port number of the MQTT broker")
    parser.add_argument("-t","--topic", required = True, help = "Topic to subscribe")
    parser.add_argument("-u","--user", required = True, help = "Username of the MQTT broker")
    parser.add_argument("-pw","--password", required = True, help = "Password for the MQTT broker")
    args = parser.parse_args()
    subscribe.callback(on_message_print, args.topic, hostname=args.host, port = args.port, auth={'username':args.user, 'password':args.password})