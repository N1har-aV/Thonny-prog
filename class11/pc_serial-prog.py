import serial
baud=115200
port='COM3'
s = serial.Serial(port, timeout = 1.0)
s.baudrate = baud
while True:
    s.write(bytes('hello', 'utf-8'))
    