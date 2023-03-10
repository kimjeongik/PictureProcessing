import cv2

### 영상 소스 열기
src1 = cv2.imread('c:/images/picture01.jpg')


### 영상 처리 알고리즘 구현####
dst1 = cv2.cvtColor(src1, cv2.COLOR_RGB2GRAY)




### 영상 디스플레이
cv2.imshow("src1", src1)
cv2.imshow("dst1", dst1)




cv2.waitKey(0)  # 아무키 누르면 사진이 꺼짐
cv2.destroyAllWindows() # 메모리 누적되는것을 삭제
