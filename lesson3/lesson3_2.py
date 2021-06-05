name = input()
age = int(input())
hobby = input()

if name == "Ali" and age > 17 and hobby == "1% of tiktok":
    print("Ты Али")
else:
    print("Ты не аЛИ, ты школьник")

if name == "Ali" or age > 17 or hobby == "1% of tiktok":
    print("Ты либо Али, либо страше 17, либо твое хобби ТИКТОК")
else:
    print("ТЫ вообще не подходишь под эти условия!")
