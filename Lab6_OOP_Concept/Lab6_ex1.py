
# class creation
class Student:
    # class attribute
    faculty = "MT"
    # init
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

# object creation attribute
    def student_info(self):
        print(f'name:{self.name} Major:{self.major} GPA:{self.gpa}')


# object creation
s1 = Student("Feen","MIT",3.00)
s2 = Student("tukta",'DBM',3.55)
# S3 = Student()
# difplay attributes object
print(s1.name,s1.major,s1.gpa)
print(s2.name,s2.major,s2.gpa)

# difplay with f-string
print(f'name:{s1.name} major:{s1.major} GPA:{s1.gpa}')
print(f'name:{s2.name} major:{s2.major} GPA:{s2.gpa}')

print(s1.faculty,s2.faculty)

# change data in object attribute
print(s1.major)

s1.major = "MG"
print(s1.major)

# abject call method in class
s1.student_info()
s2.student_info()

# list

std_list = [] # std_list = [s1,s2]
std_list.append(s1)
std_list.append(s2)
# display number of abject in list
print(len(std_list))

# for loop and list
for x in  std_list:
    x.student_info()