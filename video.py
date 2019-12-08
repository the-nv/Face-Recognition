import cv2

cap = cv2.VideoCapture("./video/vid1.mp4")
i = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    if i % 100 == 0:
        cv2.imwrite("./video/vid1/vid1_" + str(i) + ".jpg", frame)
    
    i += 1

cap.release()
cv2.destroyAllWindows()    