import paho.mqtt.client as mqtt
from datetime import datetime
from visualizer import make_html
import requests

log_file = None
data_frame = []

out_file_path = './outputs/' + datetime.strftime(datetime.now(), '%Y-%m-%d-t-%H_%M_%S')
chat_id = '111837486'
message = " "


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global log_file
    if rc == 0:

        print("Connected successfully")
        log_file = open(out_file_path + '_data.log',
                        'wt+')
    else:
        print("Connect returned result code: " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data_str = msg.payload.decode('utf-8')
    str_rcv = "Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8")
    log_file.write((str_rcv + '\n'))
    log_file.flush()
    data_frame.append((float(data_str)))
    if len(data_frame) % 4 == 0:
        make_html(data_frame, out_file_path + '.html')
    if float(data_str) > 30:
        message = "it's too hot!!🔥"
        try:
            res = requests.get(
                url="https://api.telegram.org/bot1815234860:AAHNqiI5pDl0YyIt30qLlJzXZPWbe7rVJNE/sendMessage?chat_id={}&text={}".format(
                    chat_id, message))
            print(res.json())
        except:
            pass

    if float(data_str) < 5:
        message = "it's too cold!!🥶"
        try:
            res = requests.get(
                url="https://api.telegram.org/bot1815234860:AAHNqiI5pDl0YyIt30qLlJzXZPWbe7rVJNE/sendMessage?chat_id={}&text={}".format(
                    chat_id, message))
            print(res.json())
        except:
            pass
    print(str)


# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# set username and password
# client.username_pw_set("", "")

# connect to HiveMQ Cloud on port 1883
client.connect("broker.hivemq.com", port=1883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic")

# publish "Hello" to the topic "my/test/topic"
# client.publish("my/test/topic", "Hi. I'm Pedram")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
log_file.close()
