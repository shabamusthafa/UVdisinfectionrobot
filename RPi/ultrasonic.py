import RPi.GPIO as io
import time

io.setmode(GPIO.BCM)
io_trigg= 23
io_echo= 24

print ("Distance Measurement In Progress")

io.setup(io_trigg,GPIO.OUT)
io.setup(io_echo,GPIO.IN)
io.output(io_trigg, False)

print ("Waiting For Sensor To Settle")

time.sleep(2)
io.output(io_trigg, True)
time.sleep(0.00001)
io.output(io_trigg, False)

while io.input(io_echo)==0:
    pulse_start= time.time()
while io.input(io_echo)==1:
    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance, 2)

print ("Distance:",distance,"cm")