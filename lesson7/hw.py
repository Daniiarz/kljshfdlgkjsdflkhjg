plane = [
  #   0    1    2
    ["*", "*", "*"],  # 0
    ["*", "*", "*"],  # 1
    ["*", "*", "*"]   # 2
]

plane[2][1] = "X"


def print_plane(plane):
    for i in plane:
        print(i[0], i[1], i[2])
        print("-------")


print_plane(plane)

plane[0][2] = "0"
print_plane(plane)
