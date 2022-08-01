import RPi.GPIO as GPIO
import time

SERVO_MIN_PULSE = 500
SERVO_MAX_PULSE = 2500
Servo = 12

def map(value, inMin, inMax, outMin, outMax):
    return (outMax - outMin) * (value - inMin) / (inMax - inMin) + outMin

def setup2():
    global p
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Servo, GPIO.OUT)
    GPIO.output(Servo, GPIO.LOW)
    p = GPIO.PWM(Servo, 50)
    p.start(0)

def setAngle(angle):
    angle = max(0, min(180, angle))
    pulse_width = map(angle, 0, 180, SERVO_MIN_PULSE, SERVO_MAX_PULSE)
    pwm = map(pulse_width, 0, 20000, 0, 100)
    p.ChangeDutyCycle(pwm)
def left():
    for i in range(0, 90, 5):
            setAngle(i)
            time.sleep(0.002)
            print(i)
    time.sleep(0.5)
def right():
    for i in range(90, -1, -5):
            setAngle(i)
            time.sleep(0.0001)
            print(i)
    time.sleep(0.09)
def loop():
    while True:
        left()
        right()
def destroy():
    p.stop()
    GPIO.cleanup()
def open1():
    setup2()
    left()
    p.stop()
    time.sleep(2)
    p.start(0)
    right()
    destroy()

if __name__ == '__main__':
    open1()

    #try:
        #loop()
    #except KeyboardInterrupt:
    #    destroy()