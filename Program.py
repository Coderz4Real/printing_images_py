import cv2
img ="Default"
count=1
while(count!=0):
    count=int(input("Do you want to check image details(1/0)"))
    if(count==1):
        image_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for x in range(26):
            print("Press ",x+1," to see image and details of ",image_list[x])
        image_input=int(input())
        if(image_input==1):
            img = cv2.imread("A.jpg")
        elif(image_input==2):
            img = cv2.imread("B.jpg")
        elif(image_input==3):
            img = cv2.imread("C.jpg")
        elif(image_input==4):
            img = cv2.imread("D.png")
        elif(image_input==5):
            img = cv2.imread("E.jpg")
        elif(image_input==6):
            img = cv2.imread("F.jpg")
        elif(image_input==7):
            img = cv2.imread("G.jpg")
        elif(image_input==8):
            img = cv2.imread("H.jpg")
        elif(image_input==9):
            img = cv2.imread("I.jpg")
        elif(image_input==10):
            img = cv2.imread("J.jpg")
        elif(image_input==11):
            img = cv2.imread("K.jpg")
        elif(image_input==12):
            img = cv2.imread("L.jpg")
        elif(image_input==13):
            img = cv2.imread("M.jpg")
        elif(image_input==14):
            img = cv2.imread("N.png")
        elif(image_input==15):
            img = cv2.imread("O.jpg")
        elif(image_input==16):
            img = cv2.imread("P.jpg")
        elif(image_input==17):
            img = cv2.imread("Q.png")
        elif(image_input==18):
            img = cv2.imread("R.jpg")
        elif(image_input==19):
            img = cv2.imread("S.png")
        elif(image_input==20):
            img = cv2.imread("T.png")
        elif(image_input==21):
            img = cv2.imread("U.png")
        elif(image_input==22):
            img = cv2.imread("V.png")
        elif(image_input==23):
            img = cv2.imread("W.png")
        elif(image_input==24):
            img = cv2.imread("X.jpg")
        elif(image_input==25):
            img = cv2.imread("Y.jpg")
        elif(image_input==26):
            img = cv2.imread("Z.jpg")
        else:
            img = cv2.imread("Default.jpg")
        image_resizing = cv2.resize(img,(500,500))
        cv2.imshow(" Resized Image",image_resizing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Detail about original pic")
        print("Image shape = ",img.shape)
        print("Image size = ",img.size)
        print("Data type of Image = ",img.dtype)


