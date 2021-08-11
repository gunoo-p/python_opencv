import cv2, time

# 시간 초
start_time = 0


#웹캠에서 영상을 읽어온다
cap = cv2.VideoCapture(0)   # 0일 땐 웹캠,  이미지&동영상도 넣을 수 있습니다 
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

#얼굴 인식 캐스케이드 파일 읽는다
face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')


while(True):
    # frame 별로 capture 한다
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #인식된 얼굴 갯수를 출력
    gw = len(faces)
    
            

    """
    # 0 = 사람이 없을 때
    # else = 사람이 1명 이상 있을 때
    if(gw == 0):
        print('사람이 없어요 !')
    else:
        print('안녕하세요 ~!~!')
    """
    # 인식된 얼굴에 사각형을 출력한다
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    #화면에 출력한다
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    # 0 = 사람이 없을 때
    # else = 사람이 있을 때
    if(gw == 0):
        start_time = 0      # 사람이 없어지면 0초로 초기화
        print("사람이 없어요 !")
        continue
    else:
        start_time += 1     # 1개씩 증가
        time.sleep(1)       # 1초 딜레이
        if(start_time == 3):    # 3초일 때
            print("어서오세요 ~")   
            start_time = 0      # 멘트가 나온 후 다시 0초로 초기화
            continue
    print(start_time)

cap.release()
cv2.destroyAllWindows()

