
def task1():

    number = int(input("Введите число: "))
    x = [12, 25, 33, 45, 123]
    if number in x:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


def task2():

    s = [5, 15, 22, 22, 31, 60, 60, 90]
    duplicate = {str(a) for a in s if s.count(a) > 1}
    a = lambda: print("Нет повторяющихся элементов")
    b = lambda: print("Повторяются: ", " ".join(duplicate))
    a() if len(duplicate) < 1 else b()


def task3():

    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    weekends = int(input("Введите количество выходных, которые вы хотите на неделе: "))
    print("Ваши выходные дни: ", week[:-weekends - 1:-1])
    print("Ваши рабочие дни: ", week[:-weekends])


def task4():

    import random
    input()
    MV_4 = ("Дзбоева", "Веселова", "Григорьева", "Прохоренкова", "Ленков", "Коллар", "Смирнов", "Трусова", "Денисова", "Мигунов")
    MV_5 = ("Бодрова", "Гончарова", "Крылова", "Панин", "Лындин", "Михайлова", "Карлина", "Попов", "Долгих", "Иванов")
    sport = tuple(random.sample(MV_5, 10)[:5] + random.sample(MV_4, 10)[:5])
    print("1-мв-4: ", MV_4)
    print("1-мв-5: ", MV_5)
    print("Спортивная команда: ", *sport)
    print("Количество студентов: ", len(sport))
    sport = tuple(sorted(list(sport)))
    print("Список по алфавиту: ", *sport)
    if "Иванов" in sport:
        print(list(sport).count("Иванов"), " Иванов входит в команду ")
    else:
        print("Иванов не входит в команду")


task1()
task2()
task3()
task4()
