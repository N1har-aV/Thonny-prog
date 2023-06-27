from microbit import *
uart.init(115200)
while True:
    if uart.any():
        message=uart.read()
        if message==b"on":
            pin1.write_digital(1)
        if message==b"off":
            pin1.write_digital(0)