
import RPi.GPIO as GPIO
import dht11
import time
import datetime

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 14
    DHT = dht11.DHT11(pin=14)

    while True:
        result = DHT.read()
        if result.is_valid():
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)

        time.sleep(1)

if __name__=="__main__":
        main()