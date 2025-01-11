#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

channel = 21


ALL_GPIO_PINS = list(range(2, 28))  
USED_PINS = [channel]  
UNUSED_PINS = [pin for pin in ALL_GPIO_PINS if pin not in USED_PINS]

for pin in UNUSED_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    previous_state = None  
    while True:
        current_state = GPIO.input(channel)  
        if current_state == GPIO.LOW: 
            if previous_state != "Tilt Detected": 
                print("Tilt Detected")
                previous_state = "Tilt Detected"
        else:  # No tilt
            if previous_state != "No Tilt":  
                print("No Tilt")
                previous_state = "No Tilt"
        time.sleep(0.1)  

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
