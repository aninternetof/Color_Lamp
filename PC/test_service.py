# Python 3.x service test script
import argparse
import json
import urllib.request
import urllib.parse


def Run(url, red, green, blue):
    color = {'red':red, 'green':green, 'blue':blue}
    
    req = urllib.request.Request(url)
    req.data = json.dumps(color).encode()
    req.add_header('content-length', len(req.data))
    req.method = 'POST'
    response = urllib.request.urlopen(req, timeout=5)
    
    print(vars(response))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', default='http://localhost:8081', help='LED service address')
    parser.add_argument('-r', '--red', type=int, default=100, help='Red value (0-100)')
    parser.add_argument('-g', '--green', type=int, default=100, help='Green value (0-100)')
    parser.add_argument('-b', '--blue', type=int, default=100, help='Blue value (0-100)')

    args = parser.parse_args()
    Run(args.server, args.red, args.green, args.blue)
    
