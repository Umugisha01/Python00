# Python Object-Oriented Programming


class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
# class Developer(Employee):
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first,last, pay)
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self, first, last, pay, employees = None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
        
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())


emp_1 = Employee('Bumugisha', 'christian', 700)
emp_2 = Employee('Test', 'User', 800)


print(emp_1 + emp_2)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())






# dev_1 = Developer('Bumugisha', 'christian', 700000, 'Python')
# dev_2 = Developer('Test', 'User', 80000, 'Java')


# mgr_1 = Manager('sue', 'smith', 900000, [dev_1])





# print(issubclass(Developer, Employee))

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()

