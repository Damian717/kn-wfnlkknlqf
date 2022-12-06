class parent():
    
    def _init_(self):
        print("This is parent class")
        
    def menu(dish):
        if dish=="burger":
            print("You can add the following toppings")
            print("More cheese | Add jalapeno")
        elif dish=="iced_americano":
            print("You can add the following toppings")
            print("Add chocolate flavour | Add caramel flavour")
        else:
            print("please enter valid dish")
            
    def final_amount(dish, add_ons):
        if dish=="burger" and add_ons=="cheese":
            print("you need to pay 250 USD")
        elif dish=="burger" and add_ons=="jalepeeno":
            print("you need to pay 350 USD")
        elif dish=="iced_americano" and add_ons=="chocolate":
            print("you need to pay 250 USD")
        elif dish=="iced_americano" and add_ons=="caramel":
            print("you need to pay 450 USD")
            
class child1(parent):
    
    def __init__(self,dish):
        self.new_dish = dish
        
    def  get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object=child1("burger")
child1_object.get_menu()

child2_object=child2("burger","jalepeeno")
child2_object.get_final_amount()