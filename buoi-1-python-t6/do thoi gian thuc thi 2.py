import timeit

setup = """
def reverse_slicing(s: str) -> str:
return s[::-1]
"""

code = """
reverse_slicing("Hello World")
"""

t = timeit.timeit(setup=setup, stmt=code, number=10000)
print(f"{t*1000000:6.2f} micro seconds")