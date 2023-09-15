from Evcar import evcar

    # add data
def input_evcar_data():
        id = input("Enter evcar  id: ")
        brand = input("Enter evcar brand: ")
        model = input("Enter evcar model: ")
        acc_rate = input("Enter evcar acc_rate: ")
        hp    = input("Enter evcar hp: ")
        range = input("Enter evcar range: ")
        price = float(input("Enter avcar price: "))

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