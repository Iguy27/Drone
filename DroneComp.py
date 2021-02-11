# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

#create functions here...
# Square function with a for loop
# Drone goes through first hula hoop
def first_hoop():
    sendmsg('forward 220')
#drone goes through second hoop
#def second_hoop():


#drones mission through third hula hoop with a yaw
#def third_hoop():
    #sendmsg('up 200')

#drones mission through fourth hoop
#def fourth_hoop():
    #sendmsg('up 12')
#do a flip to celebrate completion
#def celebration():
    #sendmsg('up 2000')
print("\nIsaiah Walters")
print("Program Name: Drone Competition")
print("Date: 11.13.2020")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command')
        sendmsg('takeoff',8)

        #square()
        first_hoop()
        sendmsg('land')
        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
