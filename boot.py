# boot.py -- run on boot-up
import network, utime


# Replace the following with your WIFI Credentials

ap = network.WLAN(network.WLAN.IF_AP) # create access-point interface
ap.config(ssid='IHGS') # set the SSID of the access point
ap.config(max_clients=10) # set how many clients can connect to the network
ap.active(True)         # activate the interface
while not ap.active():
    pass
print('network config: ', ap.ifconfig())

