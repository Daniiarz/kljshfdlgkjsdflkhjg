age = int(input())

if age > 18:
    name = input()
    if name == "Daniiar":
        hobby = input()
        if hobby == "drawing":
            print("Вы не умеете Петь")
        else:
            print("Вы умеете Петь")
        print("Вас зовут Данияр")
    else:
        print("Вы не Данииияр")
else:
    print("Вам нельзя!")
