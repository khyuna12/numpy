import numpy as np

'''
   다차원 열분할 ==> 수평축을 기준으로 열 분할

   1. np.hsplit(arr, n) ==> 수평(horizontal)방향으로 n개 분할
   3. np.split(arr, n , axis=1) ==> 컬럼(column)방향으로 n개 분할

'''
arr = np.arange(12).reshape(3, 4)
print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
# 1. 열 분할
column_split, column_split2 = np.hsplit(arr, 2)
print("1. column_split ", column_split)
'''
[[0 1]
 [4 5]
 [8 9]]
 '''
print("1. column_split2 ", column_split2)
'''
[[ 2  3]
 [ 6  7]
 [10 11]]
'''
column_split, column_split2 = np.split(arr, 2, axis = 1)
print("2. column_split ", column_split)
print("2. column_split ", column_split2)  # 동일

'''
   다차원 행분할 ==> 수직축을 기준으로 행 분할

   1. np.vsplit(arr, n) ==> 수직(vertical)방향으로 n개 분할
   3. np.split(arr, n , axis=0) ==> 행(row)방향으로 n개 분할

'''
arr = np.arange(12).reshape(3, 4)
print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# 2. 행분할
row_split,row_split2, row_split3 = np.vsplit(arr, 3)
print("1. vsplit(arr,3): ", row_split, row_split2, row_split3)
# [[0 1 2 3]] [[4 5 6 7]] [[ 8  9 10 11]]

row_split,row_split2, row_split3 = np.split(arr, 3, axis = 0)
print("2. split(arr,3): ", row_split, row_split2, row_split3)  # 동일
