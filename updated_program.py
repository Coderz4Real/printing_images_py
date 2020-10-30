import cv2
import os
img = "Default"
inputCount=1
def isdisplayingimage(image):
    input_image = cv2.imread(image)
    img = cv2.resize(input_image , ( 300,300 ))
    cv2.imshow(" Resized Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def isshowingproperties(image):
    img = cv2.imread(image)
    print("Image shape = ",img.shape)
    print("Image size = ",img.size)
    print("Data type of Image = ",img.dtype)    
while(inputCount!=0):
    inputCount=int(input("Do you want to check image details(1/0)"))
    if(inputCount==1):
        for image in os.listdir("."):
            isdisplayingimage(image)
            print("Pic name = "+ image)
            isshowingproperties(image)
        

