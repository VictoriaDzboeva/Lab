
def task2():

    from PIL import Image, ImageFilter
    from pathlib import Path

    current_dir = ''
    filenames = Path(current_dir).glob('*')
    Path('new_images').mkdir(parents=True, exist_ok=True)

    for file in filenames:
        if file.suffix in ['.jpg', '.png']:
            with Image.open(file) as img:
                img.load()
                new_img = img.filter(ImageFilter.CONTOUR)
                new_img.save(Path("new_images", file))

def task3():

    import csv

    file = open("data.csv", "r", encoding='windows-1251')
    data = list(csv.reader(file, delimiter=","))
    print("Нужно купить:")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
    print(f"Итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
    file.close()


task2()
task3()