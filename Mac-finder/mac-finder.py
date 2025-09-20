import requests
import time

path = "/home/ash27kan/Desktop/macs.txt"

def loader(path):
    with open(path, "r") as x:
        return x.read().splitlines()

def finder(macs):
    url =  "https://api.macvendors.com/{}".format(macs)
    response = requests.get(url)
    return response.text

def printer(macs):
    for z, mac in enumerate(macs, start=1):
        result = finder(mac)
        print("[{}]: {} -> {}".format(z, mac, result))
        time.sleep(1)

def main():
    macs = loader(path)
    printer(macs)

if __name__ == "__main__":
    main()
