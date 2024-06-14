import cv2
import time
import os
import glob


def clean_folder():
    images_path = glob.glob("images/*.png")
    for path in images_path:
        os.remove(path)


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

    differences_frame = cv2.absdiff(first_frame, gray_frame_blur)
    thresh_frame = cv2.threshold(differences_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if rectangle.any():
            status = 1

            cv2.imwrite(f"images/{count}.png", img=frame)
            count += 1

            images = glob.glob("images/*.png")
            image_index = int(len(images) / 2)

            object_image = images[image_index]



    cv2.imshow("Object Detection", frame)
