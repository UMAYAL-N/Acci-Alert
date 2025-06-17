from twilio.rest import Client
import cv2
import threading
import csv
import os
from datetime import datetime


# Twilio credentials (Replace with your actual credentials in a secure way)
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
twilio_phone_number = 'your_twilio_phone_number'
hospital_phone_number = 'hospital_contact_number'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Camera location URL
camera_location_url = "https://www.google.com/maps/@12.9791467,80.198727,3a,81.1y,172.29h,73.87t/data=!3m6!1e1!3m4!1szi7EdawuATYfNWNyD1JOwg!2e0!7i13312!8i6656?coh=205409&entry=ttu"

# Function to send SMS
def send_sms(to, body):
    print("Attempting to send SMS...")
    message = client.messages.create(
        body=body,
        from_=twilio_phone_number,
        to=to
    )
    print(f"SMS sent to {to}: {message.sid}")

# TwiML Bin URL
twiml_bin_url ='https://handler.twilio.com/twiml/EH3d3e690e90cfd11a473bd0e6602e7f9a'


"""
# Function to make a call
def make_call(to):
    print("Making a call...")
    call = client.calls.create(
        url=twiml_bin_url,
        from_=twilio_phone_number,
        to=to
    )
    print(f"Call initiated to {to}: {call.sid}")"""
def make_call(to):
    print("Making a call...")
    call = client.calls.create(
        twiml='<Response><Say>This is an accident alert. Please check the emergency location that is sent as sms.Immediate action required.</Say></Response>',
        from_=twilio_phone_number,
        to=to
    )
    print(f"Call initiated to {to}: {call.sid}")


# Function to send SMS and make call simultaneously
def notify_hospital():
    sms_body = f"Accident detected. Immediate response required. View location on Google Maps: {camera_location_url}"
    
    # Create threads for SMS and Call
    sms_thread = threading.Thread(target=send_sms, args=(hospital_phone_number, sms_body))
    call_thread = threading.Thread(target=make_call, args=(hospital_phone_number,))
    
    # Start the threads
    sms_thread.start()
    call_thread.start()
    
    # Wait for both threads to finish
    sms_thread.join()
    call_thread.join()


# Open the CSV file
with open('store.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

def writedata(video_path):
    accident_data = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Location':'https://www.google.com/maps/@12.9791467,80.198727,3a,81.1y,172.29h,73.87t/data=!3m6!1e1!3m4!1szi7EdawuATYfNWNyD1JOwg!2e0!7i13312!8i6656?coh=205409&entry=ttu',
        'video_url': video_path,  # Use video_path as URL for demonstration
        'message': 'Accident detected'
    }

    csv_file_path = 'storage.csv'
    
    # Check if the file exists and is empty
    file_exists = os.path.isfile(csv_file_path)
    file_empty = not file_exists or os.path.getsize(csv_file_path) == 0

    # Write data to CSV file
    with open(csv_file_path, mode='a', newline='') as file:
        fieldnames = ['date', 'timestamp','Location', 'video_url', 'message']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header only if the file is empty
        if file_empty:
            csv_writer.writeheader()
        
        # Write the accident data
        csv_writer.writerow(accident_data)

def readdata():
    import csv
    csv_file_path = 'storage.csv'
    
    # Check if file exists
    if not os.path.isfile(csv_file_path):
        print(f"File '{csv_file_path}' does not exist.")
        return
    
    # Open the CSV file
    with open(csv_file_path, mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Check if file is empty
        if file.readable():
            file.seek(0)
            rows = list(csv_reader)
            if not rows:
                print("The CSV file is empty.")
            else:
                # Iterate over each row in the CSV file
                for row in rows:
                    print(row)
        else:
            print("File is not readable.")

# Function to check for accident and send notification
def check_for_accident(video_path):
    print(f"Opening video file: {video_path}")
    cap = cv2.VideoCapture(video_path)
    last_frame = None
    no_movement_duration = 0
    accident_detected = False
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or unable to read video frame.")
            break
        if last_frame is not None:
            diff = cv2.absdiff(last_frame, frame)
            non_zero_count = cv2.countNonZero(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY))
            print(f"Non-zero pixel count: {non_zero_count}")

            if non_zero_count < 100000:  # Threshold for detecting movement
                no_movement_duration += 1
                print(f"No movement detected for {no_movement_duration} frames.")
                
                if no_movement_duration >10:  # Check for 10 seconds (assuming 3 fps)
                    print("No movement detected for 10 seconds. Accident suspected.")
                    accident_detected = True
                    break
            else:
                no_movement_duration = 0
                print("Movement detected, resetting no movement counter.")
        last_frame = frame
    cap.release()
    if accident_detected:
        print("Accident detected. Preparing to send notifications.")
        notify_hospital()
        writedata(video_path)
        print("storage successful")
        print("displaying storage details")
        readdata()
    else:
        print("No accident detected.")

if __name__ == "__main__":
    video_path=r"C:/Users/HP/Desktop/entries/accialert/case1vad.mp4"
    ###video_path = r"C:/Users/HP/Desktop/accialert/case1vnad.mp4"  # Path to your video file
    print("Starting accident detection...")
    check_for_accident(video_path)
    """print("Accident detection completed.")
    print("----------------------------------")
    video_path = r"C:/Users/HP/Desktop/entries/accialert/case2vad.mp4"
    ###video_path = r"C:/Users/HP/Desktop/accialert/caseAvad.mp4"  # Path to your video file
    print("Starting accident detection...")
    check_for_accident(video_path)
    print("Accident detection completed.")
    print("----------------------------------")
    print("----------------------------------")
    video_path =r"C:/Users/HP/Desktop/entries/accialert/case3vad.mp4"
    ###video_path = r"C:/Users/HP/Desktop/accialert/case2vad.mp4"  # Path to your video file
    print("Starting accident detection...")
    check_for_accident(video_path)
    print("Accident detection completed.")
    print("----------------------------------")
    print("----------------------------------")
    video_path ="C:/Users/HP/Desktop/entries/accialert/caseAvnad.mp4"
    ###video_path = r"C:/Users/HP/Desktop/accialert/caseBvad.mp4"  # Path to your video file
    print("Starting accident detection...")
    check_for_accident(video_path)
    print("Accident detection completed.")
    print("----------------------------------")
    print("----------------------------------")
    video_path ="C:/Users/HP/Desktop/entries/accialert/caseBvnad.mp4"
    ###video_path = r"C:/Users/HP/Desktop/accialert/case3vad.mp4"  # Path to your video file
    print("Starting accident detection...")
    check_for_accident(video_path)
    print("Accident detection completed.")
    print("----------------------------------")
    print("----------------------------------")
    video_path=r"C:/Users/HP/Desktop/entries/accialert/caseivadmnd.mp4"
    ###video_path = r"C:/Users/HP/Desktop/accialert/case2vad.mp4"  # Path to your video file
    print("Starting accident detection...")
    check_for_accident(video_path)
    print("Accident detection completed.")
    print("----------------------------------")"""
