class Employee:
    def  __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def employee_info(self):
        print(f'Employee name: {self.name} Salary: {self.__salary}')

    # getter and setter methods
    def get_salary(self): # read from attribute:
        return  self.__salary

    def set__salary(self,new_salary): # update data ib attribute
        self.__salary = new_salary


# class end

emp = Employee("Wanwisa",10000)
emp.employee_info()

# access to public member
print(emp.name)
#print(emp.__salary)

# name mangling
print(emp._Employee__salary)

# call to getter and setter method
print(emp.get_salary())
emp.set__salary(20000)
emp.employee_info()
