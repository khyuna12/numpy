
import numpy as np

print(np.__version__)  # 1.24.3

arr1 = [[1,2,3],[4,5,6]]
arr2D = np.array(arr1)
print("1. 2차원 행렬 생성: \n", arr2D, type(arr2D))
print("1. 벡터의 차원(dimension,axis)갯수:", arr2D.ndim) # 2
print("2. 벡터의 각 차원의 크기(shape):", arr2D.shape) # tuple로 반환 (2, 3)
print("3. 벡터의 총 요소 갯수(size):", arr2D.size)   # 6
print("4. 벡터의 저장 데이터 type(dtype):", arr2D.dtype) # int32 (4 byte )

