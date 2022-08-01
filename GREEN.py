import RPi.GPIO as GPIO
import time

LedPin = 6  # pin 11

def setup():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LedPin, GPIO.OUT)
  GPIO.output(LedPin, GPIO.HIGH)


def GREEN():
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
    setup()
    GREEN()
