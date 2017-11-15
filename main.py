import mac_address
import RPi.GPIO as GPIO
import dht11
import time
import urllib
import threading

url = "http://html.takashia.xyz/post_ESP.php"
Mac_address=mac_address.macaddress()

def post(humi,temp):
    try:
        params = {'data': str(humi),'id':Mac_address+"humi"}
        data = urllib.urlencode(params)
        d = urllib.urlopen(url, data)
        print(d)
        print("I send a message to " + url + "\nmessage:" + humi)
        params = {'data': str(temp),'id':Mac_address+"temp"}
        data = urllib.urlencode(params)
        d = urllib.urlopen(url, data)
        print(d)
        print("I send a message to " + url + "\nmessage:" + temp)
    except:
        print("I try to send a message but missed it")
        return 0
    return 0

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setup(6,GPIO.OUT)
    GPIO.output(6, True)

    # read data using pin 14
    DHT = dht11.DHT11(pin=5)

    while True:
        result = DHT.read()
        if result.is_valid():
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            threading.Thread(target=post, args=(result.humidity,result.temperature,)).start()
            time.sleep(20)
        time.sleep(1)

if __name__=="__main__":
        main()
