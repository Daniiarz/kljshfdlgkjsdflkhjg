eng_to_rus = {
    "dog": "собака",
    "cat": "кошка",
    "book": "книга",
    "table": "стол",
    "continue": "продолжить",
    "simple": "простой"
}

rus_to_eng = {
    "собака": "dog",
    "кошка": "cat",
    "книга": "book",
    "стол": "table",
    "продолжить": "continue",
    "простой": "simple"
}

rus_to_rus = {
    "собака": "собака",
    "кошка": "собака",
    "книга": "собака",
    "стол": "собака",
    "продолжить": "собака",
    "простой": "собака"
}

def translate(dictionary):
    print(dictionary)
    word = input("Слово для перевода ")
    try:
        print(f"Слово на {lang}: {word} перевод: {dictionary[word]} ")
    except KeyError:
        print("Слова нету в словаре, хотите добавить?")
        option = input()
        if option == "y":
            dictionary[word] = input(f"Перевод для слова {word} ")


while True:
    lang = input("Язык для перевода ")

    if lang == "eng":
        translate(eng_to_rus)

    if lang == "rus":
        translate(rus_to_eng)

    if lang == "rusrus":
        translate(rus_to_rus)
