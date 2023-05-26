import os.path


def task1():

    from PIL import Image

    filename = "Images/IMG_1.jpg"
    with Image.open(filename) as img:
        img.load()
        img.show()
        width, height = img.size
        format = img.format
        mode = img.mode
        print("Ширина: ", width)
        print("Высота:  ", height)
        print("Формат: ", format)
        print("Цветовая модель:", mode)

pass


def task2():

        import PIL
        from PIL import Image

        filename = "Images/IMG_2.jpg"
        with Image.open(filename) as img:
                img.load()

        new_img = img.resize((img.width // 3, img.height // 3))
        if not os.path.isdir("New Images"):
            os.mkdir("New Images")
        new_img.save("New Images/IMG_2_1.jpg")
        new_img = img.rotate(180)
        new_img.save("New Images/IMG_2_2.jpg")
        new_img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        new_img.save("New Images/IMG_2_3.jpg")


pass


def task3():


    from PIL import Image, ImageFilter
    filenames = ["Images/1.jpg, Images/2.jpg", "Images/3.jpg", "Images/4.jpg", "Images/5.jpg"]

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            if not os.path.isdir("Filter Images"):
                os.mkdir("Filter Images")
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("Filter Images/1contour.jpg")
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("Filter Images/2contour.jpg")
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("Filter Images/3contour.jpg")
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("Filter Images/4contour.jpg")
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("Filter Images/5contour.jpg")




pass


def task4():

    from PIL import Image

    water = "Images/watermark.png"
    with Image.open(water) as img_water:
        img_water.load()

    img_water = Image.open(water)
    img_water = img_water.resize((img_water.width // 2, img_water.height // 2))
    filename = "Images/4.jpg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_water, (50, 50), img_water)
    img.save("watermark4.jpg")


task1()
task2()
task3()
task4()