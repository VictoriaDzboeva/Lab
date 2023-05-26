def task1():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана -  {self.restaurant_name} \nТип кухни:{self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт!")

    newRestaurant = Restaurant("Bona Bon","")
    newRestaurant.cuisine_type = " Итальянская кухня"
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()


def task2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана -  {self.restaurant_name} \nТип кухни:{self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт!")

    Restaurant1 = Restaurant("Gudu Hogo", " Китайская кухня")
    Restaurant2 = Restaurant("L'angolo DiVino", " Итальянская кухня")
    Restaurant3 = Restaurant("Super Supper", " Испанская кухня")

    Restaurant1.describe_restaurant()
    Restaurant2.describe_restaurant()
    Restaurant3.describe_restaurant()

def task3():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, initial_rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_restaurant(self):
            print(f"Название ресторана -  {self.restaurant_name} \nТип кухни:{self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт!")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print("Рейтинг ресторана ", self.restaurant_name, "обновлен до", self.rating,
                  "\nОбновлённый рейтинг ресторана - ", self.restaurant_name, "-", self.rating)


    r = Restaurant("L'angolo DiVino", "Итальянская кухня", 4)
    print("Изначальный рейтинг ресторана", r.restaurant_name, r.rating)
    r.update_rating(5)

task1()
task2()
task3()

