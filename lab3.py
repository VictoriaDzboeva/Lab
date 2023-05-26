def task1():

    words = []

    while True:
        word = input('Введите слово: ')
        if (word == 'stop'):
            break
        else:
            words.append(word)

    print(" ".join(words))

def task2():

    while True:
        word = input('Введите слово: ')
        separated = list(word.lower())
        letter = 'ф' in separated

        if (word == 'stop'):
            break
        else:
            if letter:
                print("Ого! Это редкое слово!")
            else:
                print("Эх, это не очень редкое слово...")


def task3():

    import random

    print('Математика для детей')

    first_counter = 0
    second_counter = 0

    while second_counter < 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        answer = input(f"{a} + {b} = ")

        if answer.isdigit():
            if a + b == int(answer):
                first_counter += 1
                print('Правильно!')
            else:
                second_counter += 1
                print('Ответ неверный')
        else:
            print('Не числовое значение')

    print(f'Игра окончена. Правильных ответов: {first_counter}')


task1()
task2()
task3()