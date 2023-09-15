from EvCar import ThaiEvcar

from EvCar import ThaiEvcar

# option
def display_option():
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add ThaiEvCar")
    print("2.Delete ThaiEvCar")
    print("3.Edit ThaiEvCar model")
    print("4.Edit ThaiEvCar brand")
    print("5.Edit ThaiEvCar acceleration rate")
    print("6.Edit ThaiEvCar Hp")
    print("7.Edit ThaiEvCar range")
    print("8.Edit ThaiEvCar price")
    print("9.Display all ThaiEvCar")
    print("10.exit")
    select = int(input("select(1-10)? : "))
    if select == 1:
        input_ThaiEvCar_data()
    elif select == 2:
        delete_ThaiEvcar()
    elif select == 3:
        edit_ThaiEvcar_carid()
    elif select == 4:
        edit_ThaiEvcar_model()
    elif select == 5:
        edit_ThaiEvCar_brand()
    elif select == 6:
        edit_ThaiEvCar_accelerationrate()
    elif select == 7:
        edit_ThaiEvCar_hp()
    elif select == 8:
        edit_ThaiEvCar_range()
    elif select == 9:
        edit_ThaiEvCar_price()
    elif select == 10:
        display_ThaiEvCar()
    elif select ==11:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-11.")

    # add data
def input_ThaiEvCar_data():
        carid = input("Enter ThaiEvcar car id: ")
        model = input("Enter ThaiEvcar model: ")
        brand = input("Enter ThaiEvcar brand: ")
        accelerationrate = input("Enter ThaiEvcar acceleration rate: ")
        hp    = input("Enter ThaiEvcar hp: ")
        range = input("Enter ThaiEvcar range: ")
        price = float(input("Enter ThaiEvcar price: "))

        ThaiEvCar.my_ThaiEvCar.append(ThaiEvCar(carid,model,brand,accelerationrate,hp,range,price,))
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

# display data
def display_ThaiEvcar():
    if len(ThaiEvcar.my_ThaiEvCar) ==0:
        print("You had no ThaiEvcar data.")
    else:
        print(f'You had {len(ThaiEvCar.my_ThaiEvCar)} following:')
        n = 1 # count
        for x in  ThaiEvCar.my_ThaiEvCar:
            print(f'[{n}]',end=" ")
            x.ThaiEvcar_detail()
            n = n+1
            print("\n")

# delete ThaiEvcar
def delete_ThaiEvcar():
    # display all data in list
    display_ThaiEvcar()
    if len(ThaiEvcar.my_ThaiEvCar) == 0:
        s = int(input("Select to delete?: "))


    ThaiEvCar.delete_ThaiEvCar(ThaiEvCar, s-1)
    print("\n---------------------------------------")
    print("Your data has been deleted.")
    print("------------------------------------\n")

# edit ThaiEvcar price
def edit_ThaiEvcar_price():
    display_ThaiEvcar()
    if len(ThaiEvCar.my_ThaiEvCar) != 0:
        s = int(input("Select to edit?: "))
        # display previous price
        print(f'previous price: {ThaiEvCar.my_ThaiEvCar[s-1].price}')
        new_price = float(input("new price: "))
        ThaiEvCar.edit_ThaiEvCar_price(ThaiEvCar,s-1,new_price)
        print("\n---------------------------------------")
        print("Your data has been edited.")
        print("------------------------------------\n")

# edit ThaiEvcar price
def edit_ThaiEvcar_price():
    display_ThaiEvcar()
    if len(ThaiEvCar.my_ThaiEvCar) != 0:
        s = int(input("Select to edit?: "))
        # display previous color
        print(f'previous price: {ThaiEvCar.my_ThaiEvCar[s-1].price}')
        new_color = input("new color: ")
        ThaiEvCar.edit_ThaiEvcar_price(ThaiEvCar,s-1,new_price)
        print("\n---------------------------------------")
        print("Your data has been edited.")
        print("------------------------------------\n")

# edit ThaiEvcar brand
def edit_ThaiEvcar_brand():
    display_ThaiEvcar()
    if len(ThaiEvCar.my_ThaiEvCar) != 0:
        s = int(input("Select to edit?: "))
        # display previous brand
        print(f'previous brand: {ThaiEvCar.my_ThaiEvCar[s-1].brand}')
        new_brand = input("new brand: ")
        ThaiEvCar.edit_ThaiEvcar_brand(ThaiEvCar,s-1,new_brand)
        print("\n---------------------------------------")
        print("Your data has been edited.")
        print("------------------------------------\n")

# edit ThaiEvcar brand
def edit_ThaiEvcar_range():
    display_ThaiEvcar()
    if len(ThaiEvCar.my_ThaiEvCar) != 0:
        s = int(input("Select to edit?: "))
        # display previous range
        print(f'previous range: {ThaiEvCar.my_ThaiEvCar[s-1].range}')
        new_range = input("new range: ")
        ThaiEvCar.edit_ThaiEvcar_brand(ThaiEvCar,s-1,new_range)
        print("\n---------------------------------------")
        print("Your data has been edited.")
        print("------------------------------------\n")











# run
#my_vehicle = []
s = 0
while s == 0:
    display_option()