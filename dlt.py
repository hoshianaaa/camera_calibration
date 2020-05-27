import numpy
import csv
import pandas as pd

def calcHomography(objp, imgp):
  numPts = objp.shape[0]
  A = numpy.zeros((numPts*2, 9), float)
  imgp = imgp.reshape(numPts,2)
  for i in range(numPts):
    A[i*2+0,0:2] = objp[i,0:2]
    A[i*2+0,2] = 1.0
    A[i*2+0,6:9] = -imgp[i,0]*A[i*2+0,0:3]
    A[i*2+1,3:5] = objp[i,0:2]
    A[i*2+1,5] = 1.0
    A[i*2+1,6:9] = -imgp[i,1]*A[i*2+1,3:6]
  print(A)
  U, w, Vt = numpy.linalg.svd(A)
  print(U)
  print(w)
  print(Vt)
  return Vt[8,:].reshape(3,3)


csv_file = "data0527.csv"
csv_input = pd.read_csv(csv_file, encoding="ms932", sep=",")

imgp = csv_input[["camera_x","camera_y"]]
objp = csv_input[["world_x","world_y"]]

imgpNp = imgp.values
objpNp = objp.values

H = calcHomography(imgpNp, objpNp)
X = 410
Y = 241.5
print((H[0][0] * X + H[0][1] * Y + H[0][2]) / (H[2][0] * X + H[2][1] * Y + H[2][2]))
print((H[1][0] * X + H[1][1] * Y + H[1][2]) / (H[2][0] * X + H[2][1] * Y + H[2][2]))
