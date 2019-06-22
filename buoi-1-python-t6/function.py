def calculate(operator):
    def add(a, b):
        return a + b

    def minus(a, b):
        return a - b

    if operator == "+":
        return add
    elif operator == "-":
        return minus


print(calculate("+")(10, 2))
print(calculate("-")(10, 2))

try:
    print(calculate("***")(10, 2))
except TypeError as e:
    print(e)