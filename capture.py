import cv2
import numpy as np
import os

print("TYPE THE LETTER YOU WANT TO CAPTURE IN CAPITAL")
letter=input()
path = 'C:\\Users\\Sankalp Jain\\ML Projects\\Sign_Lang_Recog\\Dataset_Thresh\\'+letter
os.mkdir(path)
vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)
pic_no = 0
total_pic = 800
flag_capturing = False
while(vc.isOpened()):
    # read image
    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)
    x=str(pic_no)
    cv2.putText(frame,x,(50, 50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(frame, (100,100), (300,300), (0,255,0),0)
    cv2.imshow("image", frame)
    crop_img = frame[100:300, 100:300]
    blur = cv2.GaussianBlur(crop_img, (7, 7), 0)
    grey = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5))
    dilation = cv2.dilate(grey, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=1)
    final = cv2.GaussianBlur(erosion, (5, 5), 0)
    thresh = cv2.threshold(final,0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    cv2.imshow("threshold", thresh)
    if(pic_no%2==0):
        thresh=cv2.flip(thresh,1)

    if flag_capturing:
        pic_no += 1
        save_img = cv2.resize(thresh, (50,50) )
        save_img = np.array(save_img)
        cv2.imwrite(path + "/" + str(pic_no) + ".jpg", save_img)

    keypress = cv2.waitKey(1)
    if pic_no == total_pic:
        flag_capturing = False
        break    
    if keypress == ord('q'):
        break
    elif keypress == ord('c'):
        flag_capturing = not(flag_capturing)

vc.release()
cv2.destroyAllWindows()

