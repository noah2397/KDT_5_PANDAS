#--------------------------------------------------------------------
# 모듈과 패키지
# - 관계
#  * 모듈 : 특정 기능/목적의 변수, 함수, 클래스를 저장한 하나의 파이썬 파일.py
#  * 패키지 : 특정 기능/목적의 모듈들을 담고 있는 단위
# - 문법 : import 모듈명
#       : import 패키지명.모듈명
#--------------------------------------------------------------------
# 사용할 모듈 로딩 ----------------------------------------------------
import math                            # 내장 모듈, math 모듈 내 모든 변수, 함수, 클래스 다 사용한다는 의미
import math as m                       # 모듈명에 별칭을 부여해서 더 짧게 사용함
from math import factorial             # 모듈 내에서 factorial 함수만 사용하겠다는 의미
from math import factorial as fact     # 모듈 내에서 factorial 함수만 fact라는 별칭으로 사용하겠다는 의미

# 사용자 정의 함수------------------------------------------------------
def factorial(x):
    print(f'{x}!')

# 모듈 내의 요소(변수, 함수, 클래스) 사용 방법
# => 모듈명.변수
# => 모듈명.함수()
print(math.pi, math.cos(math.pi*0))  # 모듈명 째로 사용하는 방법
print(m.pi, m.cos(m.pi*0))           # 모듈명을 약칭으로 사용하는 방법
print(factorial(10))                 # 모듈 내의 함수 1개를 직접 import한 경우 바로 사용 가능
print(fact(10))                      # 모듈 내의 함수 1개를 직접 import한 경우 바로 사용 가능
