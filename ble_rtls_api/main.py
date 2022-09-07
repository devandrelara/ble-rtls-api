import paho.mqtt.subscribe as subscribe


def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))


subscribe.callback(on_message_print, "aoliveira/rtls", hostname="192.168.0.5")
