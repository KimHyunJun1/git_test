import cv2


# 동영상 파일에서 프레임을 받아온다.

capture = cv2.VideoCapture("Image/Star.mp4")



while True:
	# 현재 프레임 개수  vs 총 프레임 개수 비교



	# 현재 프레임 개수 vs 총 프레임 개수가 같으면 마지막 프레임이므로 , capture.open("")
	if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
		capture.open("Image/Star.mp4")


	ret,frame = capture.read()
	cv2.imshow("VideoFrame",frame)

	if cv2.waitKey(33) >0:
		break


capture.release()
cv2.destroyAllWindows()