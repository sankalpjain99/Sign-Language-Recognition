import cv2
import numpy as np
from keras.models import load_model

model = load_model('leg_model.h5')
gestures = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'K',
    11:'L',
    12:'M',
    13:'N',
    14:'O',
    15:'P',
    16:'Q',
    17:'R',
    18:'S',
    19:'T',
    20:'U',
    21:'V',
    22:'W',
    23:'X',
    24:'Y',
}


def predict(gesture):
    img = cv2.resize(gesture, (50,50))
    img = img.reshape(1,50,50,1)
    img = img/255.0
    prd = model.predict(img)
    index = prd.argmax()
    return gestures[index]

vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)
flag = False

while vc.isOpened():
    ret,frame = vc.read()
    if ret:        
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (100,100), (300,300), (0,255,0), 2)
        crop_img = frame[100:300, 100:300]
        blur = cv2.GaussianBlur(crop_img,(7,7),0)
        grey = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((5,5))
        dilation = cv2.dilate(grey,kernel,iterations=1)
        erosion = cv2.erode(dilation,kernel,iterations=1)
        blur1 = cv2.GaussianBlur(erosion,(5,5),0)
        thresh = cv2.threshold(blur1,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        if flag == True:
            pred_text = predict(thresh)
            cv2.putText(frame, pred_text, (30, 80), cv2.FONT_HERSHEY_TRIPLEX, 3, (0, 0, 255))
        cv2.imshow("image", frame)
        cv2.imshow("hand", thresh)
        keypress = cv2.waitKey(1)
        if keypress == ord('c'):
            flag = not(flag)
        if keypress == ord('q'):
            break

vc.release()
cv2.destroyAllWindows()

