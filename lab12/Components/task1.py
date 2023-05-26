class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название Ресторана: ",self.restaurant_name, "\nТип: ",self.cuisine_type)

    def open_restaurant(self):
        print("\nКафе открыто!")



class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        import json
        with open("ice_cream.json", "r") as read_file:
            data = json.load(read_file)
            for i in data["flavors"]:
                print("Вкус мороженого: ", i["name"])
                print("В наличии! " if i["available"] else "Нет в наличии!", "\n")

        self.flavors = ()

stand = IceCreamStand("Yum Yum", "Кафе - Мороженое")
stand.describe_restaurant()
stand.open_restaurant()
