from time import time
def reverse_slicing(s: str) -> str:
    return s[::-1]
start = time() # Danh dau thoi diem bat dau
for _ in range(10000): # Lap lai 10000 lan
    reverse_slicing("Hello World")
    delta = (time()-start) * 1000000
    print(f"{delta:6.0f} micro-seconds") # In ra thoi diem ket thuc - thoi diem bat dau
