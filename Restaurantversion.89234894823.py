# En este caso se volverá a usar el código del Reto 3 no del 7, ya que 
# en el reto se indica que se reuse el código del Reto 3:

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity: int):
        return self.price * quantity

class Beverage(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    def calculate_total_price(self, quantity: int):
        return super().calculate_total_price(quantity) * 0.1 

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, flavor: str):
        super().__init__(name, price)
        self.flavor = flavor

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, type_of_cooking: str):
        super().__init__(name, price)
        self.type_of_cooking = type_of_cooking

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, type_of_dessert: str):
        super().__init__(name, price)
        self.type_of_dessert = type_of_dessert


class Order:
    def __init__(self):
        self.items = []

    def add_items(self, item: MenuItem, quantity: int):
        self.items.append((item, quantity))

    def calculate_total_bill(self): # -> float:
        total = 0
        for item, quantity in self.items:
            total += item.calculate_total_price(quantity)
        return total
    
    def apply_discount(self, discount_percentaje: float=0):
        total = self.calculate_total_bill()
        if total > 100000:
        # Aplica un descuento adicional del 5% si el total es mayor a 100
            discount_percentaje += 10 
        elif total > 50000:
            discount_percentaje += 5
        
        discount = total * (discount_percentaje / 100)

        return total - discount
    
# Ahora la clase nueva que nos piden en el restaurant:
# y pongo los mismos items que dejé en el json del reto 7

class MenuIterable:
    def __init__(self):
        self.items = [
            MainCourse("Pizza", 21000, "Italian food"),
            MainCourse("Cheeseburger", 22000, "Fast food"),
            MainCourse("Ajiaco", 15000, "Colombian food"),
            Appetizer("Papaya", 5000, "Sweet"),
            Appetizer("Taquitos", 12000, "Salty"),
            Appetizer("Cheese fingers", 10000, "Salty"),
            Beverage("Sprite", 3000),
            Beverage("Pepsi", 5000),
            Beverage("Lemonade", 2500),
            Dessert("Chocolate Ice Cream", 5500, "Ice Cream"),
            Dessert("Vanilla Ice Cream", 4000, "Ice Cream"),
            Dessert("Cheesecake", 7000, "Cake")
        ]
    
    def __iter__(self):
        return MenuIterador(self.items)

class MenuIterador:
    def __init__(self, items):
        self.items = items
        self.indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice < len(self.items):
            item = self.items[self.indice]
            self.indice += 1
            return item
        else:
            raise StopIteration
        
menu = MenuIterable()

print("MENU")

for item in menu:
    print(f"{item.name} - ${item.price}")

    if isinstance(item, Appetizer):
        print(f"- Flavor: {item.flavor}")

    if isinstance(item, MainCourse):
        print(f"- Type of Cooking: {item.type_of_cooking}")

    if isinstance(item, Dessert):
        print(f"- Type of Dessert: {item.type_of_dessert}")

    if isinstance(item, Beverage):
        print(f"- Beverage has no extra attributes.")

    print()

orden = Order()

orden.add_items(MainCourse("Pizza", 21000, "Italian food"), 2)
orden.add_items(Appetizer("Taquitos", 12000, "Salty"), 3)
orden.add_items(Dessert("Chocolate Ice Cream", 5500, "Ice Cream"), 3)
orden.add_items(Beverage("Pepsi", 50000), 4)

print("ORDER DETAILS")
for item, quantity in orden.items:
    print(f"{item.name} x {quantity} = ${item.calculate_total_price(quantity)}")

total = orden.calculate_total_bill()
print(f"Total without discount: ${total}")

total_con_descuento = orden.apply_discount()
print(f"Total with discount: ${total_con_descuento}")