import cv2
img = "Default"
inputCount=1
def isdisplayingimage(img):
    cv2.imshow(" Resized Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def isshowingproperties(img):
    print("Detail about original pic")
    print("Image shape = ",img.shape)
    print("Image size = ",img.size)
    print("Data type of Image = ",img.dtype)    
while(inputCount!=0):
    inputCount=int(input("Do you want to check image details(1/0)"))
    if(inputCount==1):
        image_list=["A.jpg","B.jpg","C.jpg","D.jpg","E.jpg","F.jpg","G.jpg","H.jpg","I.jpg","J.jpg","K.jpg","L.jpg","M.jpg","N.jpg","O.jpg","P.jpg","Q.jpg","R.jpg","S.jpg","T.jpg","U.jpg","V.jpg","W.jpg","X.jpg","Y.jpg","Z.jpg"]
        for x in range(26):
            print("Press ",x+1," to see image and details of ",image_list[x])
        image_input=int(input())
        image_input=image_input-1
        if(image_input<=26 and image_input>=0):
            img = cv2.imread(image_list[image_input])
        else:
            img = cv2.imread("Default.jpg")
        image_resizing = cv2.resize(img,(500,500))
        isdisplayingimage(image_resizing)          #calling displaying fuction
        isshowingproperties(img)                   #calling properties function


