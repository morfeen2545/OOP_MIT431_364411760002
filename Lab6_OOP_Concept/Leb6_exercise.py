class notebook:
    def __init__(self):
        self.CPU = ""
        self.GPU = ""
        self.RAM = 0
        self.DISPLAY = ""
        self.STORAGE = ""
        self.OS = ""


        # difplay object attributes
    def notebook_info(self):
            print(f'name:{self.CPU } GPU:{self.GPU} RAM:{self.RAM} DISPLAY:{self.DISPLAY} STORAGE:{self.STORAGE} OS:{self.OS}')

s1 =  notebook() # empty object
# assign data gto object attribute
s1.CPU  = ""
s1.GPU = ""
s1.RAM = ""
s1.DISPLAY = ""
s1.STORAGE = ""
s1.OS = ""

# display  notebook data
s1.notebook_info()

# get data from user
# s2 = Student()
# s2.name = input("Enter name:")
# s2.name = input("Enter major:")
# s2.gpa = float(input("Enter GPA:"))
# s2.student_info()

nd = []

n = int(input('How many  notebook?: '))
for i in range (n):
    s =  notebook()
    print((f"Please, enter  notebook info {i+1}:"))
    s.name = input("Enter CPU:")
    s.name = input("Enter GPU:")
    s.name = input("Enter RAM:")
    s.name = input("Enter DISPLAY:")
    s.name = input("Enter STORAGE:")
    s.name = input("Enter OS:")
    nd.append(s)


# display all student in input
for i in nd:
    i.notebook_info()
