import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)

first_frame = None
status_list = []
count = 1

while True:
    check, frame = cap.read()
    cv2.imshow("Object Detection", frame)
