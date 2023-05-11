from microbit import *
uart.init(115200)
while True:
    if uart.any():
        message = uart.read()

        display.scroll(message)