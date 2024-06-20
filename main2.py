import cv2
from time import sleep

cascade_src = 'haarcascade_car.xml'
video_src = 'sudirman.mp4'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

delay= 600
detec = []
pos_line=310 
offset=10
car= 0

def center_object(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

while True:
    ret, img = cap.read()
    time = float(1/delay)
    sleep(time)
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1, minSize=(50, 50))
    cv2.line(img, (25, pos_line), (1200, pos_line), (255,127,0), 1) 
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        center = center_object(x, y, w, h)
        detec.append(center)
        cv2.circle(img, center, 4, (0, 0,255), -1)
        
        if center[1]<(pos_line+offset) and center[1]>(pos_line-offset):
            car+=1
            cv2.line(img, (25, pos_line), (1200, pos_line), (0,127,255), 3) 
    
    cv2.putText(img, "Kendaraan Lewat : "+str(car), (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
    cv2.imshow('video', img)
    
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()