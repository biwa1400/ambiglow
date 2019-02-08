__author__ = "Dabin"
__copyright__ = "Copyright 2019"

from PIL import ImageGrab
import numpy as np
import cv2


class ScreenReader():

	def getFream(self):
		# Get screep frame
		im = ImageGrab.grab()
		# conver to RGB
		imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
		return imm

if __name__ == "__main__":
	while True :
		scReader = ScreenReader()
		frame = scReader.getFream()
		#cv2.imshow('imm', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

    
