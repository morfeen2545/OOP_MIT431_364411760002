from Vehicle import Vehicle

# option
def display_option():
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Delete Vehicle")
    print("3.Edit Vehicle Price")
    print("4.Edit Vehicle color")
    print("5.Display all Vehicle")
    print("6.exit")
    select = int(input("select(1-6)? : "))
    if select == 1:
        input_vehicle_data()
    elif select ==2:
        delete_vehicle()
    elif select ==3:
        edit_vehicle_price()
    elif select == 4:
        edit_vehicle_color()
    elif select == 5:
        display_vehicle()
    elif select ==6:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-6.")

    # add data
def input_vehicle_data():
        brand = input("Enter vehicle brand: ")
        model = input("Enter vehicle model: ")
        color = input("Enter vehicle color: ")
        maxspeed = int(input("Enter vehicle max speed: "))
        price = float(input("Enter vehicle price: "))

        Vehicle.my_vehicle.append(Vehicle(brand,model,color,maxspeed,price))
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

# display data
def display_vehicle():
    if len(Vehicle.my_vehicle) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had {len(Vehicle.my_vehicle)} following:')
        n = 1 # count
        for x in  Vehicle.my_vehicle:
            print(f'[{n}]',end=" ")
            x.vehicle_detail()
            n = n+1
            print("\n")

# delete vehicle
def delete_vehicle():
    # display all data in list
    display_vehicle()
    if len(Vehicle.my_vehicle) == 0:
        s = int(input("Select to delete?: "))


        Vehicle.delete_vehicle(Vehicle, s-1)
        print("\n---------------------------------------")
        print("Your data has been deleted.")
        print("------------------------------------\n")

# edit vehicle price
def edit_vehicle_price():
    display_vehicle()
    if len(Vehicle.my_vehicle) != 0:
        s = int(input("Select to edit?: "))
        # display previous price
        print(f'previous price: {Vehicle.my_vehicle[s-1].price}')
        new_price = float(input("new price: "))
        Vehicle.edit_vehicle_price(Vehicle,s-1,new_price)
        print("\n---------------------------------------")
        print("Your data has been edited.")
        print("------------------------------------\n")

# edit vehicle price
def edit_vehicle_color():
    display_vehicle()
    if len(Vehicle.my_vehicle) != 0:
        s = int(input("Select to edit?: "))
        # display previous color
        print(f'previous color: {Vehicle.my_vehicle[s-1].color}')
        new_color = input("new color: ")
        Vehicle.edit_vehicle_color(Vehicle,s-1,new_color)
        print("\n---------------------------------------")
        print("Your data has been edited.")
        print("------------------------------------\n")






# run
#my_vehicle = []
s = 0
while s == 0:
    display_option()


