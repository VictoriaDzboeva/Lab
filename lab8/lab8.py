def task1():

    from PIL import Image

    img = Image.open("HB.jpg")
    size = img.size
    width, height = img.size
    new_img = img.crop((0, 0, width, height - 400))
    new_img.save("HB_cut.jpg")

def task2():

    from PIL import Image
    dictionary = {1: "8march.jpg", 2: "Father Day.jpg", 3: "HB.jpg"}
    print("1 - Восьмое марта, "
          "2 - День отца, "
          "3 - День Рождения")
    ans = int(input("Введите номер открытки: "))
    filename = dictionary[ans]
    with Image.open(filename) as img:
        img.load()

    img.show()


def task3():

    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя именинника: ")
    filename = "HB_cut.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("Larisa script.ttf", 200)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 5, 300),
        name + ", поздравляю ",
        font=font,
        fill='pink'
    )
    img.show()
    img.save("HB_card.png")


task1()
task2()
task3()