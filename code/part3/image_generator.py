from grabScreen import grab_screen
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
while True:
	capture_screen, image_1=grab_screen()
	#capture_screen = cv2.cvtColor(capture_screen,cv2.COLOR_RGB2GRAY)
	# plt.imshow(capture_screen, cmap='gray')
	# plt.show()
	# current_time = time.strftime("%Y%m%d-%H%M%S")
	current_time = time.time()
	cv2.imwrite("img{}.png".format(str(current_time)),capture_screen)
	time.sleep(0.09)