import numpy as np
import cv2
import videoStream

class FrameProcessor():
		
	def updateFrame(self,frame):
		self.frame = frame
		return self
		
	def left_mean(self):
		frame = self.frame
		new_frame = frame[:,0:512]
		mean = np.mean(new_frame, axis=1)
		mean = np.mean(mean, axis=0)
		return mean