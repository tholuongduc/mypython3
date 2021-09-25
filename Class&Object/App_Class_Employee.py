from Class_Employee import employee
employee01 = employee(ID="Tec01", First_name="Tho", Family_name="Luong Duc", Salary=1000)
#Print employee information
print(f'Employee Information:\n{employee01}')
#Annual Salary
annual_salary = employee01.get_annual_salary()
print("Annual Salary: ",annual_salary)
#Salary increasement
new_salary = employee01.incrase_salary(10)
print("New salary: ", new_salary)