def task1():

    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон",
                  "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Россия": "Москва",
                  "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}

    print(countries_dict)
    x = input(str("Введите страну: "))
    if x in countries_dict:
        print("Столица - ", countries_dict[x])
        for key in sorted(countries_dict):
            print(key, '- Столица', countries_dict[key])


def task2():

    alph = {
        "авеинорст": 1,
        "дклмуп": 2,
        "бгёья": 3,
        "йы": 4,
        "жзхцч": 5,
        "шэю": 8,
        "фщъ": 10
    }
    s = 0
    word = input("Введите слово: ")
    for i in word:
        for key, value in alph.items():
            if i in key:
                s += value

    print("сумма: ", s)


def task3():

    import random

    students = {"Иванов": [], "Петров": [], "Смирнов": [], "Сидоров": [], "Васильев":[], "Кузнецов":[], "Попов":[], "Федоров":[], "Лебедев":[], "Семенов":[]}
    languages = ['Русский', 'Английский', 'Французский', 'Немецкий', 'Китайский']

    for surname in students:
        random_student = random.randint(1, 3)
        for i in range(random_student):
            random_lang = random.randint(1, 3)
            if languages[random_lang] not in students[surname]:
                students[surname].append(languages[random_lang])
    print(students)
    languages_known = []
    for language in languages:
        for surname in students:
            if language in students[surname] and language not in languages_known:
                languages_known.append(language)
    print(f"Список различных языков: {sorted(languages_known)}")
    print(f'Кол-во различных языков: {len(languages_known)}')
    chinese_students = []
    for surname in students:
        if 'Китайский' in students[surname]:
            chinese_students.append(surname)

    print("Студенты, знающие Китайский: ", chinese_students)


task1()
task2()
task3()