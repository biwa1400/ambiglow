from PIL import ImageGrab
import numpy as np
import cv2
import videoStream
import frameProcess

def test1():
	scReader = videoStream.ScreenReader()
	fmProcessor = frameProcess.FrameProcessor()
	while True:
		frame = scReader.getFream()
		cv2.imshow('screen', frame)
		
		fmProcessor.updateFrame(frame)
		left_mean = fmProcessor.left_mean()
		left_mean = left_mean/255
		left_mean = np.full((100,100,3),left_mean)
		print(left_mean[1,1])
		cv2.imshow('left_mean', left_mean)		
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

			
def test2():
	a = np.array([1,2,3])
	a = np.full((3,3,3),a)
	print(a)
if __name__ == "__main__":
	test1()
