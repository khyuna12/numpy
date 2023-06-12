
import numpy as np

print(np.__version__)  # 1.24.3

### 2차원 배열 삭제
'''
      문법:
        arr = np.delete(arr, idx|fancy|slice, axis=0|1|None )

      - axis=None 이면 flatten 적용됨.
        axis=0 이면 행 제거
        axis=1 이면 열 제거

'''

arr2D = np.arange(25).reshape(5,5)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
'''
# axis 미지정시 flat 된다.
# 1. idx 이용한 삭제
# 2차원에서 axis 지정하지 않으면 자동으로 flatten 된다.
xxx = np.delete(arr2D, -1)  # 역방향
print(xxx) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

# 2. fancy 이용한 삭제
# 2차원에서 axis 지정하지 않으면 flatten 된다.
xxx = np.delete(arr2D, [0,-1])
print(xxx)  # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

# 3. slice 이용한 삭제
# 2차원에서 axis 지정하지 않으면 flatten 된다.
xxx = np.delete(arr2D, np.s_[:8])
print(xxx) # [ 8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]

# 4. idx + axis=0 이용한 삭제 ==> 행이 삭제됨
xxx = np.delete(arr2D, -1, axis=0)
print(xxx)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''

# 5. fancy + axis=0 이용한 삭제 ==> 행이 삭제됨
xxx = np.delete(arr2D, [0,-1], axis=0)
print(xxx)
'''
[[ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''

# 6. slice  + axis=0 이용한 삭제 ==> 행이 삭제됨
xxx = np.delete(arr2D, np.s_[:3], axis=0)
print(xxx)
'''
[[15 16 17 18 19]
 [20 21 22 23 24]]
'''


# 7. idx + axis=1 이용한 삭제 ==> 열이 삭제됨
xxx = np.delete(arr2D, -1, axis=1)
print(xxx)
'''
[[ 0  1  2  3]
 [ 5  6  7  8]
 [10 11 12 13]
 [15 16 17 18]
 [20 21 22 23]]
'''
xxx = np.delete(arr2D, [0,-1], axis=1)
print(xxx)
'''
[[ 1  2  3]
 [ 6  7  8]
 [11 12 13]
 [16 17 18]
 [21 22 23]]
'''
xxx = np.delete(arr2D, np.s_[:3], axis=1)
print(xxx)
'''
[[ 3  4]
 [ 8  9]
 [13 14]
 [18 19]
 [23 24]]
'''
