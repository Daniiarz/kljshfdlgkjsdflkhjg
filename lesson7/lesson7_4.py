# banana, apple, orange

def juicer(fruit):
    if fruit == "banana":
        return "banana juice"
    elif fruit == "apple":
        return "apple juice"
    elif fruit == "orange":
        return "orange juice"


def mixer(juice_list):
    fruit_dict = {
        "apple": 0,
        "orange": 0,
        "banana": 0
    }

    for i in juice_list:
        if i == "banana juice":
            fruit_dict["banana"] += 1
        if i == "orange juice":
            fruit_dict["orange"] += 1
        if i == "apple juice":
            fruit_dict["apple"] += 1

    result = ""

    for i in fruit_dict.keys():
        if fruit_dict[i] > 0:
            result += f"{i}(%.2f" % ((fruit_dict[i]*100)/3) + "%) "

    return f"{result}juice"


juice_list = []
for i in range(3):
    juice = juicer(input())
    juice_list.append(juice)

print(mixer(juice_list))
