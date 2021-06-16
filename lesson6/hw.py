import random

num = random.randint(1, 16)

print(num)
user_num = int(input())

if num-3 <= user_num <= num+3:
    print("Горячо")
