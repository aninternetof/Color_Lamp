from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from rgb_led import RgbLed
import json
from argparse import ArgumentParser

class ColorServer(HTTPServer):
	def __init__(self, *args, **kwargs):
		HTTPServer.__init__(self, *args, **kwargs)
		self.rgbLed = RgbLed('P9_14','P9_16','P9_22') #TODO: put in config file
			
class ColorRequestHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		responseType = self.headers.get('Accept', 'text/html')
		datalength = int(self.headers.get('content-length', 0))
		readData = self.rfile.read(datalength)
		if not readData:
			self.send_response(400)
			self.wfile.write('No data recieved or content-length not set')
			return
		rxDict = json.loads(readData.decode())
		for color, brightness in rxDict.items():
			if color not in self.server.rgbLed.colors:
				self.send_response(400) #bad request
				self.wfile.write('Invalid color {0}.'.format(color))
				return
			self.server.rgbLed.colors[color].setBrightness(brightness)
			self.send_response(200) #success
		if responseType == 'text/html':
			self.wfile.write('')
		elif responseType == 'none':
			pass
		return
		
def RunServer(bindaddress, port):
	print "Starting service on {0} on port {1}".format(bindaddress, port)
	service = ColorServer((bindaddress, port), ColorRequestHandler)
	try:
		service.serve_forever()
	except KeyboardInterrupt:
		print "Closing service"
	service.server_close()
	

if __name__ == '__main__':
	parser = ArgumentParser(description = 'Server for setting RGB LED color')
	parser.add_argument('-p', '--port', type=int, default=8080, help='Port number')
	parser.add_argument('-b', '--bindaddress', default='', help='Bind address, e.g. eth0') 
	args = parser.parse_args()
	
	RunServer(args.bindaddress, args.port)


			
		

