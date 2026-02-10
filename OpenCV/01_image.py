import cv2

#이미지 읽기
img = cv2.imread("images/ham1.jpg")
#이미지 창에 표시
cv2.imshow("Image Window", img)
#키보드 입력 대기(0은 무한 대기)
key = cv2.waitKey(0)
print("Pressed key code:", key)
# 모든 창 닫기
cv2.destroyAllWindows()