import cv2

delay= 600
detec = []
pos_line=300 
offset=3
car= 0


car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

# Inisialisasi video capture
cap = cv2.VideoCapture('sudirman2.mp4')

def center_object(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    #cx = x + x1
   # cy = y + y1
    cx = (x + x + w) // 2
    cy = (y + y + h) // 2
    return cx,cy

while True:
    # Ambil frame dari video
    ret, frame = cap.read()

    # Konversi ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi kendaraan
    cars = car_cascade.detectMultiScale(gray,1.4,1,minSize=(100, 100))
     
    cv2.line(frame, (25, pos_line), (1200, pos_line), (255,127,0), 3) 
    same_object_detected = False
    # Gambar kotak pembatas di sekitar kendaraan yang terdeteksi
    for (x, y, w, h) in cars:
        #dist = math.hypot(cx - pt[0], cy - pt[1])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        center = center_object(x, y, w, h)
        detec.append(center)
        cv2.circle(frame, center, 4, (0, 0,255), -1)

        if center[1]<(pos_line+offset) and center[1]>(pos_line-offset):
            car+=1
            cv2.line(frame, (25, pos_line), (1200, pos_line), (0,127,255), 3) 
    
    cv2.putText(frame, "Kendaraan Lewat : "+str(car), (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
    print("Hitung Kendaraan:"+str(car))
    # Tampilkan frame yang telah dianotasi
    cv2.imshow('Car Detection', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Tutup video capture dan jendela tampilan
cap.release()
cv2.destroyAllWindows()