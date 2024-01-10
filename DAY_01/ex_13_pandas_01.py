# 판다스 패키지 설치 확인 및 버전 체크
#---------------------------------------------
#
import pandas as pd


# 버전 확인--------------------------------------
print(pd.__version__)

# 데이터 파일 읽기 -------------------------------

# 상대경로 : 현재 파일을 기준으로 잡아서 경로를 설정
filename='../DATA/used_cars.csv'
data=pd.read_csv(filename)
print(f'data => {type(data)}, {data}') # 데이터 타입 및 데이터 출력