age = 20


def a_b(a, b):
    c = a + b
    print(age)


def a_b2(a, b):
    c = a + b
    return c


def a_mul_b(a, b):
    c = a * b
    return c


result1 = a_b(1, 3)
result2 = a_b2(a_b2(1, 4), a_mul_b(1, 5))

print("-------")
print(result1)
print(result2)
