def task1():
    password = input('Введите пароль: ')

    is_numeric = False
    is_upper = False
    is_lower = False
    is_special = False

    for char in password:
        if char.isnumeric():
            is_numeric = True
        elif char.islower():
            is_lower = True
        elif char.isupper():
            is_upper = True
        elif char in "@#%&!":
            is_special = True

    if len(password) > 4 and is_numeric and is_upper and is_lower and is_special:
        print('Пароль принят')
    else:
        print('Пароль не принят')


def task2():

     n = int(input("Введите номер места: "))
     if n < 37:
          print("Купе")
     else:
          print("Боковое место")

     if n % 2==0:
          print("Верхнее место")
     else:
          print("Нижнее место")

def task3():

     Year = int(input("Введите год: "))
     if Year % 4 == 0 and (Year % 100) % 4 == 0:
          print (f"Год {Year} високосный")
     else:
          print ("Этот год не високосный")

def task4():
    one_color, two_color, = input('Первый цвет: '), input('Второй цвет: ')
    colors = ['красный', 'синий', 'фиолетовый', 'желтый', 'оранжевый', 'зеленый']
    res_color = 'Не верно введены цвета'
    if one_color in colors[:3] and two_color in colors[:3]:
        res_color = one_color if one_color == two_color else colors[colors.index(one_color) + colors.index(two_color) + 2]
    print(res_color)

def task5():
    words = []

    N = int(input("Кол-во слов: "))

    while N >= 1:
        word = input('Введите слово: ')
        words.append(word)
        N -= 1

    print(" ".join(words))


task1()
task2()
task3()
task4()
task5()