
def task1():

    x = int(input("Введите число: "))
    if x % 3 == 0:
        print("Делится")
    else:
        print ("Не делится")

def task2():

    try:
        x = int(input("Введите число: "))
    except ValueError:
        print("Введите число!")
        task2()
        return
    try:
        x/x
    except ZeroDivisionError:
        print("Число не делится!")
        task2()
        return
    if x % 100 == 0:
        print("Делится")
    else:
        print("Не делится")
def task3():

    from datetime import date, datetime

    x = datetime.strptime(input("Введите дату: "), "%d.%m.%Y")
    if str(x.day * x.month) == str(x.year)[2:]:
        print("wOw! Магическая дата")
    else:
        print("Это не магическая дата")

def task4():

    a = [int(i) for i in input()]
    if len(a) % 2 != 0:
        print("Введите четное количество чисел: ")
        task4()
        return
    if sum(a[:int(len(a)/2)]) == sum(a[int(len(a)/2):]):
        print("Ура! Счастливый билет!")
    else:
        print("Не счастливый билет")

task1()
task2()
task3()
task4()