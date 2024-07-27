class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.cook_time=15

class Burger(Food):
    def __init__(self, name, price,meat,ingredients):
        super().__init__(name, price)
        self.meat=meat
        self.ingredients=ingredients

class Pizza(Food):
    def __init__(self, name, price,size,toppings):
        super().__init__(name, price)
        self.size=size
        self.toppings=toppings

class Drinks(Food):
    def __init__(self, name, price, isCold=True):
        super().__init__(name, price)
        self.isCold=isCold

class Menu:
    def __init__(self):
        self.pizzas=[]
        self.burgers=[]
        self.drinks=[]

    def add_menu_item(self, item_type, item):
        if item_type == "pizza":
            self.pizzas.append(item)
        elif item_type=="burger":
            self.burgers.append(item)
        elif item_type=="drinks":
            self.drinks.append(item)
    
    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        
    def show_menu(self):
        for i in self.pizzas:
            print(f'name: {i.name} , price: {i.price}')
        
        for j in self.burgers:
            print(f'name: {j.name} , price: {j.price}')

        for k in self.drinks:
            print(f'name: {k.name} , price: {k.price}')
            
        
        


        