import numpy as np

'''
    벡터연산(Vectorized operation)
    1. 기존 파이썬에서 지원 안된 요소간의 연산을 numpy는 지원함
    2. 다차원배열간 산술연산, 다차원배열과 스칼라 산술연산
    3. 비교연산도 가능 ==> 논리값 ==> boolean 색인 (중요)
        ==> and/or/not 대신에 &/|/~ 사용한다
        
    브로드캐스팅(Broadcasting)
    -> 서로 다른 차원을 가지고 있는 두개의 값을 산술하는 도중에 
    연산이 가능하도록 차원을 자동으로 맞추어 주는 작업을 의미한다
'''

# 1. 기본 파이썬 연산
print("1. 파이썬의 리스트 + 리스트")
print([10,20,30]+[10,20,30])  #[10, 20, 30, 10, 20, 30]

print("2. 기본 파이썬의 리스트 + 스칼라")
# print([10,20,30] + 2)  # TypeError: can only concatenate list (not "int") to list
print([10,20,30] * 3)  # [10, 20, 30, 10, 20, 30, 10, 20, 30]

##############################################################
# 2. 다차원배열 + 다차원배열 ==> 요소간 연산, 반드시 shape 일치해야 된다.
arr1D_1 = np.array([10,20,30])
arr1D_2 = np.array([5,4,3])
print("3. numpy의 벡터간 연산 처리")
print(arr1D_1 + arr1D_2)  # [15 24 33]
print(arr1D_1 - arr1D_2)  # [ 5 16 27]
print(arr1D_1 * arr1D_2)  # [50 80 90]
print(arr1D_1 / arr1D_2)  # [ 2.  5. 10.]

# 3. 백터 + 스칼라 ==> 자동으로 브로드캐스팅 되어 연산됨.
arr1D_1 = np.array([10,20,30])
print("4. numpy의 벡터 + 스칼라 연산 처리")
print(arr1D_1 + 2)  # [12 22 32]
print(arr1D_1 - 2)  # [ 8 18 28]
print(arr1D_1 * 2)  # [20 40 60]
print(arr1D_1 / 2)  # [ 5. 10. 15.]

# 4. 비교 연산도 벡터화 가능 ==> boolean 색인 적용 가능 (중요)
print("5. 벡터의 비교 연산처리1: ", arr1D_1%3 == 0) # [False False  True]
print("5. 벡터의 비교 연산처리2: ", arr1D_1 > 15) # [False  True  True]
print("5. 벡터의 비교 연산처리3: ", (arr1D_1 > 15) & (arr1D_1%6 == 0)) # [False False  True]
