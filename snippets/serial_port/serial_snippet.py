#make sure to instal requirements and activated the venv
import serial 

# we may have to use sudo to access this port
ser = serial.Serial("/dev/ttyACM0", 9600)

# read some value from the serial port
val = ser.readline()

# print it or send it away with mqtt
print(val)

