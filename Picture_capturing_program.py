import cv2
import time
def capturingimages(count):
    capture = cv2.VideoCapture(0)
    while True:
        ret , frame = capture.read()
        cv2.imshow("frame",frame)
        if(cv2.waitKey(0)):
            image_name=str(count)+".jpg"
            cv2.imwrite(image_name,frame)
            break
    capture.release()
    cv2.destroyAllWindows()
count=1
while(count<=5):
       capturingimages(count)
       time.sleep(5)
       count=count+1
