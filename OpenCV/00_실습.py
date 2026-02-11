#원본 이미지 가로세로 절반으로 축소
# 1번 이미지를 좌우 반전
# 2번 이미지를 원본과 동일한 크기의 복사이미지의 우하단에 배치

import cv2

image = cv2.imread('OpenCV/images/ham1.jpg')

# #가로 세로 축소
# img_down = cv2.pyrDown(image)

# #좌우 반전
# img_flip = cv2.flip(image, 1) # > 0 : Y축 반전

# cv2.imshow('Flip 1',img_flip)
# cv2.imshow('Down 2', img_down)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#실습 답안

if image is None:
    print("파일을 찾을 수 없습니다.")
else:
    h,w,_ = image.shape

    # 2분의 1 축소
    small_img = cv2.resize(image, (w // 2, h //2))
    #좌우 반전
    flipped_img = cv2.flip(small_img, 1)
    #우하단 배치
    result = image.copy()
    sh, sw, _ = flipped_img.shape

    #시작점부터 이미지 높이만큼만 영역 지정
    result[h//2 :h//2+sh, w//2 : w//2+sw] = flipped_img

    cv2.imshow('Result',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()