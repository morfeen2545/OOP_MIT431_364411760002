class Vehicle:
    #class attribute
    #my_vihecle = []
    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price =price
        # self.my_vihecle.append(self)


        # difplay object attributes
    def Vehicle_info(self):
            print(f'brand:{self.brand} '
                  f'model:{self.model} '
                  f'color:{self.color} '
                  f'maxspeed:{self.maxspeed}'
                  f' price:{self.price}')
# std = []
# n = int(input('How attributes Vehicle?: '))
# for i in range (n):
#     s =  Vehicle()
#     print((f"Please, enter Vehicle info :"))
#     s.brand = input("Enter brand:")
#     s.model = input("Enter model:")
#     s.color = input("Enter color:")
#     s.maxspeed = input("Enter max speed")
#     s.price = input("Enter price:")
#     v.Vehicle
#
#
# # display all Vehicle in input
# for i in vc:
#     i.Vehicle_info()