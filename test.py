import cv2
import numpy as np
import face_recognition

imgSania = face_recognition.load_image_file('C:\Face-Recognition-Attendance-System\Face-Recognition-Based-Attendance-System\Images_Attendance\Sania Mirza.jpg')
imgSania = cv2.cvtColor(imgSania, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('C:\Face-Recognition-Attendance-System\Face-Recognition-Based-Attendance-System\Images_Attendance\Sania Mirza test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgSania)[0]
encodeModi = face_recognition.face_encodings(imgSania)[0]
cv2.rectangle(imgSania, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

facelocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

results = face_recognition.compare_faces([encodeModi], encodeTest)
faceDis = face_recognition.face_distance([encodeModi], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('Sania Mirza', imgSania)
cv2.imshow('Sania Mirza test', imgTest)
cv2.waitKey(0)