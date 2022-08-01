import RPi.GPIO as GPIO
import time

LedPin = 19  # pin 11

def setup1():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LedPin, GPIO.OUT)
  GPIO.output(LedPin, GPIO.HIGH)


def RED():
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(LedPin, GPIO.LOW) # led off
    time.sleep(1)
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(LedPin, GPIO.LOW) # led off
    time.sleep(1)
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(LedPin, GPIO.LOW) # led off
    GPIO.cleanup()


if __name__ == '__main__':     # Program start from here
    setup1()
    RED()