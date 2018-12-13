#Import Relevant Libraries.

import RPi.GPIO as GPIO
from time import sleep
import board
import busio
from adafruit_ads1x15.single_ended import ADS1115

#SetUp Raspberry Pi I/O Pins.

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)
pwm = GPIO.PWM(18,50)
input_state = GPIO.input(27)
pwm.start(0)


#Initialising I2C Connection with the ADS1115 ADC.
#Set GAIN for ADC.

class MainController:
    def __init__(self):
        self.DoorStatus = "Open"
        self.GAIN = 2/3
        self.i2c = busio.I2C(board.SCL,board.SDA)
        self.adc = ADS1115(self.i2c)


#Valve Adjustment According to Status of the Door.
        
    def ValveControl(self):
        input_state = GPIO.input(27)
        if input_state == False:
            pwm.start(0)
            if self.DoorStatus == "Open":
                print("Door Closing")
                #potentiometer_one = self.adc.read_volts(0,gain = self.GAIN, data_rate=None)
                #duty = potentiometer_one * 4
                duty = 90/18 +2
                GPIO.output(18,True)
                pwm.ChangeDutyCycle(duty)
                sleep(0.5)
                self.DoorStatus = "Closed"
                GPIO.output(18,False)
                pwm.ChangeDutyCycle(0)
                print("Door Closed")
                sleep(2)
                
            elif self.DoorStatus == "Closed":
                print("Door Opening")
                #potentiometer_two = self.adc.read_volts(1,gain = self.GAIN, data_rate=None)
                #duty1 = potentiometer_two * 4
                duty1 = 180/18 +2
                GPIO.output(18,True)
                pwm.ChangeDutyCycle(duty1)
                sleep(0.5)
                self.DoorStatus = "Open"
                GPIO.output(18,False)
                pwm.ChangeDutyCycle(0)
                print("Door Opened")
                sleep(2)

                
            else:
                print("ERROR")
        else:
            pass

            
valvecontroller = MainController()
while input_state == True:
    valvecontroller.ValveControl()

