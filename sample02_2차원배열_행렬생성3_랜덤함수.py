
import numpy as np

print(np.__version__)  # 1.24.3

# 1) 랜덤값 고정
np.random.seed(1234)

# 2) np.random.random(size=(행,열))
print("1. random(size=(행,열))")
arr = np.random.random(size=(2,3))
print(arr, type(arr), arr.dtype)

# 3) np.random.rand(행, 열)
'''
def rand(*dn: Any) -> Any
rand(d0, d1, ..., dn)
'''
print("2. rand(행, 열)")
arr = np.random.rand(2, 3)  # 튜플로 넣으면 안됨
print(arr, type(arr), arr.dtype)

# 4) np.random.randn(행,열)
print("3. randn(행,열)")
arr = np.random.randn(2, 3)
print(arr)

# 5) np.random.randint(low, high, size=(행,열))
print("4. randint(1,10,size=(행,열))")
arr = np.random.randint(1,10, size=(2,3))
print(arr)

# 6) np.random.randint(high, size=(행,열))
print("4. randint(5, size=(행,열)): ")
arr = np.random.randint(5, size=(2,3))  # 0~4
print(arr)

# 7) np.random.choice(리스트)
print("5. np.random.choice(['foo','bar','baz']")
choice_value = np.random.choice(['foo','bar','baz'])
print(choice_value)

# 8) np.random.shuffle(리스트)
# 주어진 리스트를 shuffle 함.  in-pacle(True)로 동작됨.
print("6. np.random.shuffle(1,3,56,7,98])")
shuffle_value = [1,3,56,7,98]
np.random.shuffle(shuffle_value)
print(shuffle_value)

