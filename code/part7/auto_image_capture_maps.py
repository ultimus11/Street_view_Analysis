import cv2
import numpy as np
from pynput.mouse import Button, Controller
import time
from direct_key_inputs import PressKeyPynput, ReleaseKeyPynput, W, A, S, D
from grabScreen import grab_screen

# imp note scan code are available here for key inputs: 
# https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)?redirectedfrom=MSDN
# don't use VK codes

mouse=Controller()

def mouse_paint():
	#Rectangle 
	mouse.position=(200,500)    #(Xposition, Yposition)
	mouse.press(Button.left)
	time.sleep(0.5)
	mouse.position=(300,500)
	time.sleep(0.5)
	mouse.position=(300,300)
	time.sleep(0.5)
	mouse.position=(200,300)
	time.sleep(0.5)
	mouse.position=(200,500)
	mouse.release(Button.left)
# mouse_paint()

#following func is for forward movement
def forward():
	time.sleep(1)
	PressKeyPynput(W)
	time.sleep(0.7)
	ReleaseKeyPynput(W)
	time.sleep(1)

#following func navigates 360 degree
def capture_and_navigate():
	rotation=1
	#captures images 8 times
	while rotation<=8:
		rotation+=1
		time.sleep(2)
		PressKeyPynput(D)
		time.sleep(0.7)
		ReleaseKeyPynput(D)
		time.sleep(1)
		capture_screen, image_1=grab_screen()
		time.sleep(1)
		cv2.imwrite("captured_img/strt{}.png".format(time.time()),capture_screen)
		#time.sleep(0.5)
capture_and_navigate()
forward()
capture_and_navigate()