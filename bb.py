import cv2

capture=cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while True:
	ret,frame = capture.read()
	cv2.imshow("VideoCapture",frame)
	if cv2.waitKey(1) > 0:
		break

capture.release()
cv2.destroyAllWindows()C:\Users\June Kim\AppData\Local\Programs\Python\Python37-32