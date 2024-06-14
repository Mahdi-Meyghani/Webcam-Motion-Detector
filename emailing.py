import smtplib
from email.message import EmailMessage
import os

USER = "mahdimeyghani02@gmail.com"
PASSWORD = os.getenv("WebcamObjectDetectionPassword")
RECEIVER = "mahdimeyghani02@gmail.com"
HOST = "smtp.gmail.com"
PORT = 587


def send_email(img_path):
    with open(img_path, "rb") as f:
        binary_img = f.read()

    email_msg = EmailMessage()

    email_msg["Subject"] = "New customer Entered"
    email_msg.set_content("Wow! What a customer :)")
    email_msg.add_attachment(binary_img, maintype="image", subtype="png")

    email = smtplib.SMTP(host=HOST, port=PORT)

    email.ehlo()
    email.starttls()
    email.login(USER, PASSWORD)
    email.sendmail(USER, RECEIVER, email_msg.as_string())
    email.quit()


if __name__ == "__main__":
    send_email("images/new.jpg")
