age = [19, 25, 3, 90]
age2 = (19, 25, 3, 90)
# age3 = []
#
# for i in range(2):
#     age = int(input())
#     age3.append(age)
#     print(age3)

# names = []
# for i in range(4):
#     name = input()
#     names.append(name)
#
# for i in names:
#     print(i)

# print(age3)

password = input()

while len(password) < 8:
    print("Ошибка пароля")
    password = input()


name = input()

while name != "Altynai":
    name = input()
