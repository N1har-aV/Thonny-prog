from microbit import *
while True:
    moisture_level=pin1.read_analog()
    sleep(30)
    print(moisture_level)
     