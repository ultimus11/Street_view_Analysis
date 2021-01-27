from pynput.mouse import Button, Controller
import time
from direct_key_inputs import PressKeyPynput, ReleaseKeyPynput, W, A, S, D

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
mouse_paint()
# time.sleep(2)
# PressKeyPynput(W)
# ReleaseKeyPynput(W)
# PressKeyPynput(0x24)
# ReleaseKeyPynput(0x24)
