import numpy as np

'''
    1. 다차원 열병합 ==> 수평축을 기준으로 열 병합
      ** 튜플 형태로 들어간다는 거 주의**

   1. np.hstack((arr, arr2)) ==> 수평(horizontal)방향으로 병합
   2. np.concatenate((arr,arr2), axis=1 ) ==> axis=1인 컬럼방향으로 병합
   3. np.column_stack((arr, arr2)) ==> 컬럼(column)방향으로 병합
    
    2. 다차원 행병합 ==> 수직축을 기준으로 행 병합

   1. np.vstack((arr, arr2)) ==> 수직(vertical)방향으로 병합
   2. np.concatenate((arr,arr2), axis=0 ) ==> axis=0인 행방향으로 병합
   3. np.row_stack((arr, arr2)) ==> 행(row)방향으로 병합
    
    
    
'''

# 1. 다차원 열병합
arr = np.arange(9).reshape(3,3)
arr2 = arr * 2
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 '''
print(arr2)
'''
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''
column_merge = np.hstack((arr,arr2))
print(column_merge)
''' 꼬치
[[ 0  1  2  0  2  4]
 [ 3  4  5  6  8 10]
 [ 6  7  8 12 14 16]]
'''
column_merge2 = np.concatenate((arr,arr2) , axis=1)
print(column_merge2)
column_merge3= np.column_stack((arr, arr2))
print(column_merge3)  # 셋다 결과 똑같음

# 2. 다차원 행병합
arr = np.arange(9).reshape(3,3)
arr2 = arr * 2
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 '''
print(arr2)
'''
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''
row_merge = np.vstack((arr,arr2))
row_merge2 = np.concatenate((arr,arr2) , axis=0)
row_merge3= np.row_stack((arr, arr2))
print("1. vstack(튜플): \n",row_merge)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''