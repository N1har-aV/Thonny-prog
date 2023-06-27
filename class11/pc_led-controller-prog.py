import serial
baud=115200
port='COM4'
s = serial.Serial(port, baud, timeout = 1.0)
#s.baudrate = baud
while True:
    led_state=input("state of the LED\n")
    s.write(bytes(led_state, 'utf-8'))
    
