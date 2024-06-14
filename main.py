import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)

first_frame = None
status_list = []
count = 1

while True:
    check, frame = cap.read()

    status = 0

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_blur = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_blur


    cv2.imshow("Object Detection", frame)
