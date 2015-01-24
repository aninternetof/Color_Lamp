import Adafruit_BBIO.PWM as PWM

class Led:
	def __init__(self, name, pin, brightness):
		self.name = name
		self.pin = pin
		self.brightness = brightness
	def turnOn(self):
		PWM.start(self.pin, self.brightness)
	def turnOff(self):
		PWM.stop(self.pin, self.brightness)
	def setBrightness(self, brightness):
		self.brightness = brightness
		PWM.set_duty_cycle(self.pin, brightness)

class RgbLed:
	def __init__(self, pinR, pinG, pinB):
		ledR = Led('red', pinR, 0)
		ledG = Led('green', pinG, 0)
		ledB = Led('blue', pinB, 0)
		self.colors = {}
		self.colors[ledR.name] = ledR
		self.colors[ledG.name] = ledG
		self.colors[ledB.name] = ledB
		self.turnOn()
		print "------ RGB LED initialized -----"

	def __del__(self):
		PWM.cleanup()
		print "----- PWM is all cleaned up! See ya. -----"

	def turnOn(self):
		for l in self.colors.values():
			l.turnOn()

	def turnOff(self):
		for l in self.colors.values():
			l.turnOff()

	def makeWhite(self, brightness):
		for l in self.colors.values():
			l.setBrightness(brightness);

	def resumeColor(self):
		for l in self.colors.values():
			l.setBrightness(l.brightness)
		

#l = RgbLed('P9_14','P9_16','P9_22')
#l.makeWhite(100)
#raw_input()

