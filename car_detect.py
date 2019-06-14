# Image Processing

# 1. 번호판 위치 알아내기
# 2. tesseract library

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 글씨 읽기
import pytesseract


# BGR -> GRAY
# Threshold (GaussianBlur, adaptiveThreshold )
#              노이즈 줄이기         이미지의 threshold 값을 주어 그래프를 극단적으로 (직각형태로 만듬)
#                                                        검은색과 흰색으로 나누어 ( 컴퓨터가 찾기 쉽게 )
# Contours(윤곽선 찾기)
# 각 윤곽선들의 (x,y,w,h) 구함 (무수히 많은 윤곽선)
# 번호판 글자 크기 대략 가정 하여 (Area,Width,height,ratio 설정)
# 각 윤곽선들 중 지정한 값에 해당하는 윤곽선들을 따로 추출 (번호판 확률 높은 것들)
# 번호판 글자 처럼 생긴 애들만 남는다 
# 남긴 애들의 위치 배열을 보고서 진짜 번호판 일거 같은 것들 추려냄 (일렬로 배열 (각도나 크기 변화 있지만, 대부분 순차적))
# 윤곽선 끼리의 거리 제한, 두 윤곽선 중심점끼리의 각도, 면적의 차이, 너비 차이, 높이 차이,  <- 모두 통과한 윤곽선 최소한 3개 이상만 번호판 인정
# 위에 해당하는 윤곽선의 index들만 리스트에 넣어준다
# 후보군을 그리면 번호판 배열 윤곽선만 남는다.
# Affine Transform 사용하여 기울어진 배열을 동일선상으로 위치시킨다 (삐뚤어진 각도를 구하여 첫번째와 마지막 번호판의 센터 잡고)
# 번호판 부분만 추출
# Threshold 후 한번더 윤곽선 찾기 (확실하게 하려고)



# pytesseract.image_to_string  ( chars = pytesseract.image_to_string(img_result,lang='kor',config='--psm 7 --oem 0'))


