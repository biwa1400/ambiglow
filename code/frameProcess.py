__author__ = "Dabin"
__copyright__ = "Copyright 2019"

import numpy as np
import cv2
import videoStream

class FrameProcessor():
		
	def updateFrame(self,frame):
		self.frame = frame
		return self
		
	def left_mean(self):
		frame = self.frame
		#--get screen leftside(1366/2*768) pixel 0-255 BGR
		new_frame = frame[:,0:683]
		mean = np.mean(new_frame, axis=1)
		mean = np.mean(mean, axis=0)
		return mean
		
	def right_mean(self):
		frame = self.frame
		#--get screen rightside(1366/2*768) pixel 0-255 BGR
		new_frame = frame[:,683:1366]
		mean = np.mean(new_frame, axis=1)
		mean = np.mean(mean, axis=0)
		return mean