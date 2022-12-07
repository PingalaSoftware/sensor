from gpiozero import MotionSensor
from gpiozero import LED
white_led=LED(17)
mvs= MotionSensor(4)
white_led.off()
print("start")
while True:
        mvs.wait_for_motion()
        print("Motion detected")
        white_led.on()
        mvs.wait_for_no_motion()
        white_led.off()
        print("No motion detected")