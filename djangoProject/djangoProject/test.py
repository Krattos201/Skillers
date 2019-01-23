import cv2

cap=cv2.VideoCapture(0)

def beginStream():
	while True:
		ret,frame = cap.read()
		cv2.imshow("SEE HERE",frame)