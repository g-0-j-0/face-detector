import cv2,time as t

hj=0
video=cv2.VideoCapture(cv2.CAP_DSHOW)
fc=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
a=1
sample=0
while True:
    a+=1
    check,frame=video.read()
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        sample += 1
        hj=cv2.imwrite("dataSet/User." + str(id) + "." + str(sample) + ".jpg", gray[y:y + h, x:x + w])
        img=cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 6)
    if hj==True:
        print("duhhhh",a)
   # print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
    cv2.imshow("captured",frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break

print(a)
video.release()
cv2.destroyAllWindows()