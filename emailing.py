import smtplib
from email.message import EmailMessage
import os

USER = "mahdimeyghani02@gmail.com"
PASSWORD = os.getenv("WebcamObjectDetectionPassword")
RECEIVER = "mahdimeyghani02@gmail.com"
HOST = "smtp.gmail.com"
PORT = 587


def send_email(img_path):
    pass