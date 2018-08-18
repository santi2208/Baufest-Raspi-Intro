import RPi.GPIO as GPIO
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
import sys

class MainSwitchController(object):
	def TurnOnSwitch(self, gpioPort):
		print('FUNCTION: TurnOnSwitch')

	def TurnOffSwitch(self, gpioPort):
		print('FUNCTION: TurnOffSwitch')	

if __name__ == '__main__':
