import paho.mqtt.client as mqtt
from gpiozero import LED, Button
from signal import pause
from time import sleep
import urllib2



led = LED(17)
button_pressed = Button(2)

client = mqtt.Client()
client.connect('broker.hivemq.com', 1883, 60)

def button_press():
	print 'message sent!'
	client.publish('test/richie', " WOMAN IN LABOUR")
	urllib2.urlopen("https://maker.ifttt.com/trigger/woman_inlabour/with/key/mth3UwjXe5RsyLclHaatC4562E8gL5JIujqqmn2Q0KH").read()

button_pressed.when_pressed = button_press


pause()

