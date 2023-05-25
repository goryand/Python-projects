from employeeClass import CreateEmployee, CreateHourlyEmployee, CreateSalaryEmployee, CreateCommissionEmployee

class Company:
    def __init__(self):
        self.Employees = []

    def addEmployee(self, newEmployee):
        self.Employees.append(newEmployee)

    def payEmployees(self):
        print("Paying employees..")
        for iEmployee in self.Employees:
            print("Weekly Paycheck for: " + iEmployee.firstName + " " + iEmployee.lastName)
            print(f'Amount:  ${iEmployee.calculatePaycheck():,.2f}')
            print("-------")


# Main


myCompany = Company()

myCompany.addEmployee(CreateCommissionEmployee("Dwight", "Schrute", 85000, 250, 5))  # Dwight schrute is the top salesman! Of course he gets paid more than his other salesman!
myCompany.addEmployee(CreateCommissionEmployee("Jim", "Halpert", 85000, 150, 5))

myCompany.addEmployee(CreateSalaryEmployee("Michael", "Scott", 120000))
myCompany.addEmployee(CreateSalaryEmployee("David", "Wallace", 500000))

myCompany.addEmployee(CreateHourlyEmployee("John", "Doe", 25, 50))
myCompany.addEmployee(CreateHourlyEmployee("Tom", "Brady", 40, 15))

print(myCompany.Employees)

# Print all the company employees
for i in myCompany.Employees:
    print(i.firstName, i.lastName)

print("I want to pay my peeps!")
myCompany.payEmployees()



