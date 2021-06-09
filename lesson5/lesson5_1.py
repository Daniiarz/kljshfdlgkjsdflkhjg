d = {
    "pet": ["питомец", "погладить по голове"],
    "let's gooooo": ['поехали', 'погнали'],
    "fly": ["муха", "летать"],
    "dictionary": {
        "cat": "кошка",
        "dog": "собака"
    }
}

word = d['fly']
for i in range(len(word)):
    print(f"Значение {i+1}: {word[i]}")


word2 = d['dictionary']
print(word2)