from urllib.request import urlopen
import numpy as np
import pytesseract
import cv2
from RED import *
from GREEN import *
import RPi.GPIO as GPIO
from time import sleep
import sys
from barierre import *
minArea = 500
color = (0,255,255)
count = 0
url = r'http://192.168.247.240/capture'
plateCascade = cv2.CascadeClassifier("Resources/haarcascade_plate_number.xml")
def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

while True:
    img_resp = urlopen(url)
    imgnp = np.asarray(bytearray(img_resp.read()), dtype="uint8")
    img = cv2.imdecode(imgnp, -1)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.3, 5)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgRoi)
            custom_config = r'--oem 3 --psm 9 outputbase digits'
            text= pytesseract.image_to_string(imgRoi, config=custom_config)
            text = ''.join(e for e in text if e.isalnum())
            print(text, end=" ")
            if check_if_string_in_file('./Database/Database.txt', text) and text != "":
                print('Registered')
                #winsound.Beep(frequency, duration)
                setup()
                GREEN()
                open1()


            else:
                print("Not Registered")
                setup1()
                RED()


    cv2.imshow("Result", img)
    #text = pytesseract.image_to_string(img,config='--oem 3 -c tessedit_char_whitelist=0123456789',lang="ara")
    #text = pytesseract.image_to_string(img,config='--psm 11',lang="ara")

   # return text

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg", imgRoi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "SCAN SAVED", (150,265),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1

    elif cv2.waitKey(1) & 0xFF ==ord('q'):
        break

    else:
        pass