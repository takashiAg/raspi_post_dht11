import mac_address
import RPi.GPIO as GPIO
import dht11
import time
import urllib
import threading

url = "http://html.takashia.xyz/post_ESP.php"
Mac_address = mac_address.macaddress()


def post(humi, temp):
    try:
        params = {'data': str(humi), 'id': Mac_address + "humi"}
        data = urllib.urlencode(params)
        d = urllib.urlopen(url, data)
        print(d.read())
        print("I send a message to " + url + "\nmessage:" + str(humi))
        params = {'data': str(temp), 'id': Mac_address + "temp"}
        data = urllib.urlencode(params)
        d = urllib.urlopen(url, data)
        print(d.read())
        print("I send a message to " + url + "\nmessage:" + str(temp))
    except:
        print("I try to send a message but missed it")
        return 0
    return 0


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, True)

    # read data using pin 14
    DHT = dht11.DHT11(pin=5)
    i=0
    temp=0
    humi=0
    while True:
        print(i)
        print(humi)
        print(temp)
        result = DHT.read()
        if result.is_valid():
            temp+=result.temperature
            humi+=result.humidity
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            i+=1
        if i>=30:
            threading.Thread(target=post, args=(temp/30, humi/30,)).start()
            humi=0
            temp=0
            i=0
        time.sleep(1)


if __name__ == "__main__":
    main()
