__author__ = "Dabin"
__copyright__ = "Copyright 2019"

from PIL import ImageGrab
import numpy as np
import cv2
import videoStream
import frameProcess
import colorsys
import hueLight
import time

def test1():
	#--screen reader & processor
	scReader = videoStream.ScreenReader()
	fmProcessor = frameProcess.FrameProcessor()
	#--light
	light_right = hueLight.Light(1,'N-ooTd-KQ6oRls3zAF9S2jG4DLJsonrgaccR4eqQ')
	light_left = hueLight.Light(2,'N-ooTd-KQ6oRls3zAF9S2jG4DLJsonrgaccR4eqQ')
	light_middle = hueLight.Light(3,'N-ooTd-KQ6oRls3zAF9S2jG4DLJsonrgaccR4eqQ')
	
	# --light setting
	light_right.transitiontime(0)
	light_left.transitiontime(0)
	
	while True:
		#--get frame
		frame = scReader.getFream()
		#cv2.imshow('screen', frame)
		
		#--update frame
		fmProcessor.updateFrame(frame)
		
		#--setting_left
		mean = fmProcessor.left_mean()
		mean = mean/255
		light_left.color_rgb(mean[2],mean[1],mean[0])
		
		mean_full = np.full((100,100,3),mean)
		#print(mean_full[1,1])
		cv2.imshow('left_mean', mean_full)		
		
		
		#--setting_right
		mean = fmProcessor.right_mean()
		mean = mean/255
		light_right.color_rgb(mean[2],mean[1],mean[0])
		
		mean_full = np.full((100,100,3),mean)
		#print(mean_full[1,1])
		cv2.imshow('right_mean', mean_full)	
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		time.sleep(0.1)

	
if __name__ == "__main__":
	test1()
