# Webcam Object Detection and Image Processing Application

## Overview
This Python application is designed to interact with your computer's webcam to detect objects entering the view. Upon detection, it draws a rectangle around the object. When the object leaves the view, the application captures images, selects the best one, and sends it to your email address in real time.

## Features
- **Object Detection**: Utilizes the webcam to monitor and detect objects entering the field of view.
- **Rectangle Annotation**: Draws a rectangle around the detected object for better visibility.
- **Image Capture**: Takes multiple pictures of the object once it exits the view.
- **Image Selection**: Chooses the best picture based on predefined criteria.
- **Email Notification**: Sends the selected image to a specified email address immediately.

## Requirements
- Python 3.6 or higher
- OpenCV library
- SMTP library for email functionality

## Installation
To install the required libraries, run the following command:
`pip install -r requirements.txt`

## Usage
To start the application, run the main.py file.

## LICENSE
This project is licensed under the MIT License - see the `LICENSE.md` file for details.


## Configuration
Before running the application, configure your email settings in the `emailing.py` file:
```python
USER = "your_email@example.com"
PASSWORD = "your_password"
HOST = "smtp.example.com"
PORT = 587
```

## Acknowledgments
- Thanks to the open-source community for providing the necessary libraries and tools.
- Please replace the placeholders with your actual email settings and ensure you handle your credentials securely. Also, make sure to include any additional instructions or dependencies that are specific to your application. If you need further customization or additional sections, feel free to let me know!
