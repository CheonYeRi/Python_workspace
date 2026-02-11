import cv2
import os

# # 이미지 읽기 (흑백으로 로드)
# img = cv2.imread(r"C:\Users\heclo\Python_workspace\OpenCV\images\ham1.jpg",cv2.IMREAD_GRAYSCALE)

# # 1 고정 크기로 조정 (가로 320, 세로 240)
# dst_fixed = cv2.resize(img, (320,240))

# # 2 비율로 조정 (가로 0.5배, 세로 0.5배)
# dst_ratio = cv2.resize(img, None, fx=0.5, fy=0.5)

# cv2.imshow("Fixed Resize", dst_fixed)
# cv2.imshow("Ratio Resize", dst_ratio)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#영상 리사이즈 출력 실습
path = os.path.join(os.path.dirname(__file__), "images", "KakaoTalk_103029122.mp4")
cap = cv2.VideoCapture(path)

fps = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened(): #영상이 정상적으로 열려있을 동안 반복
    ret, frame = cap.read() #프레임 읽기

    if not ret: # 더 이상 프레임이 없으면 종료
        break

    #1.5배 리사이즈, 보간법 -INTER_CUBIC 적용
    frame_resize = cv2.resize(frame, None, fx=1.5 ,fy= 1.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Video Player", frame_resize)

    if cv2.waitKey(int(fps // 2)) >= 0:
        break

cap.release() #자원 해제
cv2.destroyAllWindows()