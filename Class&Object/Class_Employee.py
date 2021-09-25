#Define class employee
class employee:
    ID = ""
    First_name = ""
    Family_name = ""
    Salary = 0
    def __init__(self, ID, First_name, Family_name, Salary):
        self.ID = ID
        self.First_name = First_name
        self.Family_name = Family_name
        self.Salary = Salary

    def get_full_name(self):
        full_name = f'{self.Family_name} {self.First_name}'
        return full_name
    def get_salary(self):
        employee_salary = self.Salary
        return employee_salary
    def get_annual_salary(self):
        annual_salart = self.Salary * 12
        return annual_salart
    def incrase_salary(self, percent):
        print("Salary Increasement: ", percent,"%")
        new_salary = self.Salary + (self.Salary * percent)/100
        return new_salary
    def __str__(self):
        return f'ID: {self.ID}\nFull name: {self.get_full_name()}\nSalary: {self.Salary}'
