class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Название ресторана: ",self.restaurant_name,"\nТип:  ", self.cuisine_type)
    def open_restaurant(self):
        print("Кафе открыто!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.time = time


    import json

    type_for_add = int(input("Сколько вкусов мороженого вы хотите добавить: "))
    products = {"flavors": []}
    for i in range(type_for_add):
        name = input("Название: ")
        available = bool(input("В наличии - 1, не в наличии - 0:  "))
        products["flavors"].append({"name": name, "available": available})
    with open("ice_cream.json", "r") as file:
        data = json.load(file)
    data["flavors"].extend(products["flavors"])
    for i in data["flavors"]:
        print("Название: ", i["name"])
        print("В наличии" if i["available"] else "Нет в наличии!", "\n")
    with open("ice_cream.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    type_for_del = str(input("Введите вкус мороженого, который вы хотите убрать: "))
    with open("ice_cream.json", "r") as file:
        data = json.load(file)
    minimal = 0
    for txt in data['flavors']:
        if txt['name'] == type_for_del:
            data['flavors'].pop(minimal)
        else:
            None
        minimal = minimal + 1
    with open("ice_cream.json", "w") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Вкус {flavor} доступен в меню")
        else:
            print(f"Вкуса {flavor} нет в меню")

    class Cone:
        def __init__(self, flavors_cone):
            self.flavors_cone = flavors_cone

        def list_cone(self):
            print("Список доступных вкусов мороженого в рожке:", ", ".join(self.flavors_cone))

        def add_flavor_cone(self, flavor):
            self.flavors_cone.append(flavor)

        def remove_flavor_cone(self, flavor):
            self.flavors_cone.remove(flavor)

        def check_flavor_cone(self, flavor):
            if flavor in self.flavors_cone:
                print(f"Вкус {flavor} доступен в меню")
            else:
                print(f"Вкуса {flavor} нет в меню")

    class Stick:
        def __init__(self, flavors_stick):
            self.flavors_stick = flavors_stick

        def list_stick(self):
            print("Список доступных вкусов мороженого на палочке:", ", ".join(self.flavors_stick))

        def add_flavor_stick(self, flavor):
            self.flavors_stick.append(flavor)

        def remove_flavor_stick(self, flavor):
            self.flavors_stick.remove(flavor)

        def check_flavor_stick(self, flavor):
            if flavor in self.flavors_stick:
                print(f"Вкус {flavor} доступен в меню")
            else:
                print(f"Вкуса {flavor} нет в меню")

    class Scoop:
        def __init__(self, flavors_scoop):
            self.flavors_scoop = flavors_scoop

        def list_scoop(self):
            print("Список доступных вкусов мороженого в шариках:", ", ".join(self.flavors_scoop))

        def add_flavor_scoop(self, flavor):
            self.flavors_scoop.append(flavor)

        def remove_flavor_scoop(self, flavor):
            self.flavors_scoop.remove(flavor)

        def check_flavor_scoop(self, flavor):
            if flavor in self.flavors_scoop:
                print(f"Вкус {flavor} доступен в меню")
            else:
                print(f"Вкуса {flavor} нет в меню")

ice_cream = IceCreamStand("", "Кафе - Мороженое","[Chocolate, Vanilla, Mint Chocolate, Strawberry, Mango, Blueberry, Caramel, Banana, Cookies and Cream, Coffee, Nut, Peach]","ул. Сладкая д.34", "8:00 - 22:00")
print(f'Где мы находимся: {ice_cream.location}')
print(f'Режим работы: {ice_cream.time}')

ice_cream.check_flavor(input('Введите вкус мороженого для проверки наличия: '))
print()

print(f'Где мы находимся: {ice_cream.location}')
print(f'Режим работы: {ice_cream.time}')
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
print()

IceCreamCone = ice_cream.Cone(['chocolate', 'vanilla', 'mint chocolate'])
IceCreamCone.list_cone()
IceCreamCone.add_flavor_cone(input('Введите вкус мороженого в рожке , для добавления в список: '))
print()
IceCreamCone.list_cone()
IceCreamCone.remove_flavor_cone(input('Введите вкус мороженого в рожке, для удаления из списка: '))
print()
IceCreamCone.list_cone()
IceCreamCone.check_flavor_cone(input('Введите вкус мороженого в рожке для проверки наличия: '))
print()


IceCreamStick = ice_cream.Stick(['strawberry', 'mango', 'blueberry', 'banana', 'cookies and cream'])
IceCreamStick.list_stick()
IceCreamStick.add_flavor_stick(input('Введите вкус мороженого на палочке, для добавления в список: '))
print()
IceCreamStick.list_stick()
IceCreamStick.remove_flavor_stick(input('Введите вкус мороженого на палочке, для удаления из списка: '))
print()
IceCreamStick.list_stick()
IceCreamStick.check_flavor_stick(input('Введите вкус мороженого на палочке для проверки наличия: '))
print()

IceCreamScoop = ice_cream.Scoop(['coffee', 'nut', 'peach', 'caramel'])
IceCreamScoop.list_scoop()
IceCreamScoop.add_flavor_scoop(input('Введите вкус мороженого в шариках, для добавления в список: '))
print()
IceCreamScoop.list_scoop()
IceCreamScoop.remove_flavor_scoop(input('Введите вкус мороженого в шариках, для удаления из списка: '))
print()
IceCreamScoop.list_scoop()
IceCreamScoop.check_flavor_scoop(input('Введите вкус мороженого в шариках для проверки наличия: '))
print()

