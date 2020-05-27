import numpy as np
import cv2
import glob
import sys
import os

import csv

nline = 3
ncol = 3 

cap = cv2.VideoCapture(0)
corners = []

while(True):
  ret, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

  ret, corners = cv2.findChessboardCorners(gray, (nline, ncol), None)

  if ret is True:
    cv2.drawChessboardCorners(frame, (nline, ncol), corners, ret)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'start',(int(corners[0][0][0]), int(corners[0][0][1] - 10)), font, 1,(255,0,0),2,cv2.LINE_AA)

    print()
    print("**** corners ****")
    print(corners)

  cv2.imshow('frame',frame)

  key = cv2.waitKey(1) & 0xFF
  if key == ord('q'):
    break

  if key == ord('s'):
    f = open('data.csv', 'w')
    writer = csv.writer(f)

    print(corners)
    writer.writerow(["camera_x","camera_y","world_x","world_y","world_z"])
    for corner in corners:
      writer.writerow([corner[0][0], corner[0][1]])


cap.release()
cv2.destroyAllWindows()

'''
  corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
  print(corners2)
'''
