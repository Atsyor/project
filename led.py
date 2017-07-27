from gpiozero import LED, Button
import paho.mqtt.client as mqtt
from signal import pause
from time import sleep
import urllib2


led=LED(17)

def dot():
        led.on()
        sleep(3)
        led.off()
        sleep(0.1)

def dash():
        led.on()
        sleep(3)
        led.off()
        sleep(1)
     

def w():
        dot()
        dash()
        dash()
        dot()

def e():
        dot()
        dash()
        dot()
def a():
        dot()
        dot()
def r():
        dash()
        dot()
def e():
        dash()
        dot()
        dash()
        dot()
def c():
        dash()
        dot()
        dash()
        dot()



def o():
	dot()
        dash()
        dot()

def m():
	dot()
        dash()
        dot()

def i():
	dot()
        dot()

def n():
	dash()
        dot()

def g():
	dash()
        dot()
        dash()


def notification():
        w()
        e()
        a()
        r()
        e()
        c()
	o()
	m()
	i()
	n()
	g()

def on_message(client, userdata, message):
	print message.payload
	notification()

def on_connect(client, userdata, flags, code):
	print "connected:" + str(code)
	client.subscribe("test/log_out")
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)


client.loop_forever()
