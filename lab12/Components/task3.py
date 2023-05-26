from tkinter import *

class IceCreamStand:
    def __init__(self, location, time):
        self.location = location
        self.time = time
        self.flavors = []
    def add_flavor(self, flavor):
        self.flavors.append(flavor)
    def remove_flavor(self, flavor):
        self.flavors.remove(flavor)
    def check_flavor(self, flavor):
        return flavor in self.flavors

class IceCreamApp:
    def __init__(self, ice_cream):
        self.ice_cream = ice_cream

        self.root = Tk()
        self.root.title("Кафе - Мороженое")

        self.info_frame = Frame(self.root, padx=10, pady=5)
        self.info_frame.grid(row=0, column=0, sticky=W)

        self.flavors_label = Label(self.info_frame, text="Вкусы:")
        self.flavors_label.pack(anchor=W)
        self.flavors_var = StringVar()
        self.flavors_var.set(", ".join(self.ice_cream.flavors))
        self.flavors_listbox = Listbox(self.info_frame, listvariable=self.flavors_var)
        self.flavors_listbox.pack(anchor=W)
        self.flavor_entry = Entry(self.info_frame, width=20)
        self.flavor_entry.pack(side=LEFT, padx=5)
        self.add_button = Button(self.info_frame, text="Добавить", command=self.add_flavor)
        self.add_button.pack(side=LEFT)
        self.remove_button = Button(self.info_frame, text="Удалить", command=self.remove_flavor)
        self.remove_button.pack(side=LEFT)

        self.info_frame2 = Frame(self.root, padx=10, pady=5)
        self.info_frame2.grid(row=0, column=1, sticky=E)

        self.root.mainloop()

    def add_flavor(self):
        flavor = self.flavor_entry.get().strip()
        if flavor != "" and not self.ice_cream.check_flavor(flavor):
            self.ice_cream.add_flavor(flavor)
            self.flavors_var.set(", ".join(self.ice_cream.flavors))

    def remove_flavor(self):
        flavor = self.flavors_listbox.get(ACTIVE)
        if flavor != "" and self.ice_cream.check_flavor(flavor):
            self.ice_cream.remove_flavor(flavor)
            self.flavors_var.set(", ".join(self.ice_cream.flavors))

ice_cream = IceCreamStand("Невский пр. д.52", "8:00 - 21:00")
ice_cream.add_flavor("Chocolate")
ice_cream.add_flavor("Vanilla")
ice_cream.add_flavor("Mint chocolate")


app = IceCreamApp(ice_cream)






