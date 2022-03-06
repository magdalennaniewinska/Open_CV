import cv2 as cv

img = cv.imread("Source/Photos/lady.jpeg")
#cv.imshow("Person", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Grey", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

# rectangle with detected face
faces_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

# how many faces was detected
print(f"Number of faces found = {len(faces_rectangle)}")

for (x,y,w,h) in faces_rectangle:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow("Detected face", img)

cv.waitKey(0)
