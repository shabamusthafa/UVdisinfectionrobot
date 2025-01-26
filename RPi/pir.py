import RPi.GPIO as io
import time

io.setwarnings(False)
io.setmode(io.BOARD)
io.setup(11, io.IN) #Read output from PIR motion sensor
while True:
    i = io.input(11)
    if i == 0: #When output from PIR sensor is LOW
        print ("No intruders",i)
        time.sleep(0.1)
    elif i == 1: #When output from PIR sensor is HIGH
        print ("Intruder detected",i)
        time.sleep(0.1)