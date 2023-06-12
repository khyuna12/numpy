
import numpy as np

print(np.__version__)  # 1.24.3

# 1차원 배열 삭제
'''

     1. ndarray 삭제

      문법:                       색인           축(다차원일 떄)
        arr = np.delete(arr, idx|fancy|slice, axis )

      - 삭제된 새로운 배열을 반환(in-place=False)
      - axis=None 이면 flatten 적용됨.(다차원이 1차원으로)
      - slice인 경우에는  np.s_[::2]  형식 사용한다.


     2. 값으로 삭제

        - np.where( (arr==5) | (arr==8)) 활용하여 일치하는 인덱스를 먼저 찾고 삭제한다.

'''

# 1. idx|fancy|slice 삭제
print("1. idx로 삭제")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr,0)
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [8 7 5 4 3]

print("2. fancy 삭제")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr, [0,3,5] ) # fancy 인덱싱
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [8 7 4]

print("3. slice 삭제,  np.s_[::2]")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr, np.s_[0:4] ) # slice 삭제
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [4 3]

# 2. 값으로 삭제하는 방법
arr = np.array([9,8,7,5,4,3])
xx = np.delete(arr, np.where(arr == 5))  # 5 값 삭제,
print(arr)  # [9 8 7 5 4 3]
print(xx)  # [9 8 7 4 3]

print(np.where(arr == 5))  # (array([3], dtype=int64),)
print(np.where((arr == 5)|(arr==8)))  # (array([1, 3], dtype=int64),)

arr = np.array([9,8,7,5,4,3])
xx = np.delete(arr, np.where((arr==5)|(arr==8))) # 5 와 8 값 삭제,
print(arr) #[9 8 7 5 4 3]
print(xx) # [9 7 4 3]