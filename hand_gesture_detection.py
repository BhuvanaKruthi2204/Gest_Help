import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'  
smtp_port = 587  
smtp_username = 'xxx@gmail.com'  # Replace with your email
smtp_password = '123456'   # Replace with your email password

sender_email = 'xx@gmail.com'  # Replace with your email
recipient_email = 'xxx@gmail.comm'  # Replace with recipient email

subject = 'Emergency Notification'
message = 'There is an emergency situation that requires immediate attention. Please respond promptly.'
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

model = load_model('mp_hand_gesture')  
with open('gesture.names', 'r') as f:
    classNames = f.read().splitlines()

print(classNames)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera could not be opened. Exiting...")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Frame not captured. Exiting...")
        break

    x, y, c = frame.shape
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(framergb)
    className = ''

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                landmarks.append([lmx, lmy])

            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            try:
                prediction = model.predict(np.array([landmarks]))
                classID = np.argmax(prediction)
                className = classNames[classID]
            except Exception as e:
                print(f"Error during prediction: {str(e)}")

            if className.lower() == 'help':
                try:
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(sender_email, recipient_email, msg.as_string())
                    server.quit()
                    print("Notification sent successfully.")
                except Exception as e:
                    print("Failed to send the notification: " + str(e))

    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Output", frame) 

    if cv2.waitKey(1) == ord('q'):
        print("Exiting program.")
        break

cap.release()
cv2.destroyAllWindows()

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2q'  