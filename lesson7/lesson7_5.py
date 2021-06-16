def a():
    def b():
        def c():
            print("c")
            a()
            b()
        print("b")
        c()
    b()
    print("a")


def a_b(a, b, c):
    print(a)
    print(b)
    print(c)
    return a * b * c


print(a_b(a=2, b=1, c=4))
