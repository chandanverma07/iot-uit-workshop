import RPi.GPIO as GPIO
import time
import csv
import datetime
import boto3
import time
# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG = 23
ECHO = 24

# Set up the GPIO channels
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    duration = end_time - start_time
    distance = duration * 17150  # Speed of sound in air (34300 cm/s) / 2
    return distance
def write_to_csv(distance):
    with open('distance_data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), distance])
def upload_to_s3(file_name, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)

bucket_name = 'your-s3-bucket-name'

while True:
    distance = get_distance()
    write_to_csv(distance)
    upload_to_s3('distance_data.csv', bucket_name)
    time.sleep(60)  # Adjust the delay as needed
