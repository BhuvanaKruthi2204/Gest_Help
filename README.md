# Gest_Help 

**Gest_Help** is a real-time hand gesture recognition system built using Python, MediaPipe, and TensorFlow. It detects specific hand gestures like "Help" and automatically sends an emergency email notification to a predefined recipient.

---

## 💡 Features
- 🖐️ Real-time hand gesture detection using webcam
- 🧠 Deep learning model for accurate gesture classification
- 📧 Sends emergency email alerts when "Help" gesture is detected
- 🔒 Simple and secure alert mechanism using SMTP

---

## 🛠️ Tech Stack
- Python
- OpenCV
- MediaPipe
- TensorFlow / Keras
- SMTP (for email alerts)

---

## 📁 Project Structure
Gest_Help/
├── mp_hand_gesture/ # Trained model directory
├── data.pickle # Pickled dataset
├── gesture.names # List of gesture classes
├── hand_gesture_detection.py # Main script
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore config
└── README.md # Project overview


---

## 🧪 How to Run

1. 🔧 Install the dependencies:
```bash
pip install -r requirements.txt

2.🚀 Run the script:
python hand_gesture_detection.py

3.📸 Show your hand gesture in front of the webcam. If the "Help" gesture is detected, an emergency email will be sent.

📧 Email Alert Setup
To enable the alert system, open hand_gesture_detection.py and update:

python
Code:
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_app_password'
sender_email = 'your_email@gmail.com'
recipient_email = 'recipient_email@example.com'


👀 Demo
<img width="1023" height="712" alt="image" src="https://github.com/user-attachments/assets/fddf8d46-e501-4d68-ad8f-cac1b8d2dd76" />

## 👩‍💻 Author

**Mareddy Bhuvana Kruthi**  
Passionate about AI, Python, and meaningful tech 

