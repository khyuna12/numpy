
import numpy as np

print(np.__version__)  # 1.24.3

# np.arange
'''
   np.arange + reshape
 
'''

print("1. arange(10)")
data = np.arange(10).reshape((2,5))  # [0,10)형식으로 표현
print(data)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]