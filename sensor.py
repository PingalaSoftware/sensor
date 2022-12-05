from gpiozero import MotionSensor

mvs= MotionSensor(4)

while True:
	mvs.wait_for_motion()
	print("Motion detected")
	mvs.wait_for_no_motion()
	print("No motion detected")