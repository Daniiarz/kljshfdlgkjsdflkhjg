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

while True:
    lang = input("Язык для перевода ")

    if lang == "eng":
        word = input("Слово для перевода ")
        try:
            print(f"Слово на {lang}: {word} перевод: {eng_to_rus[word]} ")
        except KeyError:
            print("Слова нету в словаре, хотите добавить?")
            option = input()
            if option == "y":
                eng_to_rus[word] = input(f"Перевод для слова {word} ")

    if lang == "rus":
        word = input("Слово для перевода ")
        try:
            print(f"Слово на {lang}: {word} перевод: {rus_to_eng[word]} ")
        except KeyError:
            print("Слова нету в словаре")
            print("Слова нету в словаре, хотите добавить?")
            option = input()
            if option == "y":
                rus_to_eng[word] = input(f"Перевод для слова {word} ")
