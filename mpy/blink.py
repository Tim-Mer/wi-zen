from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
<<<<<<< HEAD
print("Finished.")
=======
print("Finished.")
>>>>>>> 722c92d503a8b5b41c97849747a57a351533378a
