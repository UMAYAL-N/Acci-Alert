# 🚨 AcciAlert: Real-Time Accident Detection & Emergency Notification System

AcciAlert is an intelligent Python-based accident detection and alert system that utilizes video analysis to detect road accidents in real time. Upon detecting an accident, it instantly notifies emergency services via SMS and automated phone calls, including the precise Google Maps location, and logs the event into a storage CSV for records.



## 📌 Why AcciAlert?

**The Problem:**
In most road accidents, the delay in medical attention significantly increases the chances of fatality. In remote or poorly monitored areas, such delays become more critical due to the lack of immediate witnesses or alert mechanisms.

**The Solution:**
AcciAlert solves this problem by constantly monitoring CCTV/video footage, detecting suspicious inactivity (like no movement post-crash), and immediately alerting nearby hospitals or emergency services.



## 🔧 How It Works

1. **Video Monitoring:** Uses OpenCV to analyze accident-related video files.
2. **Motion Detection:** Identifies abnormal scenarios by checking for absence of motion for over 10 seconds.
3. **Emergency Alert:**
   * Sends an **SMS** with a Google Maps location.
   * Initiates a **voice call** using **Twilio API**.
4. **Data Logging:** Logs all accident events (time, location, video file) into a CSV file.
5. **Console Feedback:** Outputs step-by-step analysis and status in the terminal.



## 🚀 Features

* 📹 Real-time video input analysis using OpenCV
* 📞 Twilio integration for automated emergency phone calls
* 📩 SMS alert with live location map link
* 🧠 Simple accident detection logic based on inactivity
* 📊 CSV-based structured event logging
* 🔀 Supports multiple video case files



## 📁 File Structure

accialert/
│
├── original.py           # Main Python script for accident detection and alert
├── case1vad.mp4          # Accident video - Scenario 1 (Accident Detected)
├── case2vad.mp4          # Accident video - Scenario 2 (Accident Detected)
├── case3vad.mp4          # Accident video - Scenario 3 (Accident Detected)
├── caseAvnad.mp4         # Normal video - No Accident Detected (A)
├── caseBvnad.mp4         # Normal video - No Accident Detected (B)
├── caseivadmnd.mp4       # Accident with movement detected (victim is active or people in the area helped the victim) - so no need of emergency services
├── storage.csv           # Log file storing accident records (date, time, location, video)
└── README.md             # Project overview and usage instructions



## ▶️ How to Run

### ✅ Requirements:

* Python 3.6+
* OpenCV (`cv2`)
* Twilio (`twilio`)
* Internet connection for API calls

### 🔄 Install dependencies:

bash
pip install opencv-python twilio


### 🔀 Run the script:

Update the `video_path` at the bottom of `accialert.py` to point to the required file.

Then run:

bash
python accialert.py


## 📊 Sample Data (`storage.csv`)

| Date       | Timestamp | Location                                                            | Video URL           | Message           |
| ---------- | --------- | ------------------------------------------------------------------- | ------------------- | ----------------- |
| 2024-06-14 | 14:32:10  | [Google Maps](https://www.google.com/maps/@12.9791467,80.198727...) | accident\_case1.mp4 | Accident detected |


## 🔐 Notes

* Your Twilio credentials and hospital phone numbers are hardcoded — ensure you **remove/replace** sensitive values before pushing publicly.
* The video path is currently local — adjust it if you shift to cloud-based storage (e.g., Drive links).
* Ensure test videos simulate real accident patterns (especially lack of motion).



## 🌱 Future Enhancements

* Use actual CCTV stream inputs
* ML-based accident recognition models (beyond just motion detection)
* Web dashboard to monitor logs and real-time alerts
* Auto-upload videos to Google Drive with access links in the log



## 📞 Contact

Created by **Umayal Natarajan**
📧 Email: numayalnatarajan@gmail.com
🌐 GitHub: https://github.com/UMAYAL-N
📍 Based in India



 “Saving one life is as if saving all of humanity.” — The AcciAlert Team ❤️
