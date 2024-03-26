"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import adafruit_motor
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
my_servo2 = servo.Servo(pwm2)

while True:
    my_servo.angle = 0
    my_servo2.angle = 0
    time.sleep(2)
    my_servo.angle = 180
    my_servo2.angle = 180
    time.sleep(2)
'''
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)# Write your code here :-)
'''
