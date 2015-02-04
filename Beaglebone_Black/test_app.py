from rgb_led import RgbLed

l = RgbLed('P9_14','P9_16','P9_22')
#l.makeWhite(100)
#raw_input()

while(True):
	for color in l.colors.values():
		input = raw_input(color.name)
		color.setBrightness(float(input))
