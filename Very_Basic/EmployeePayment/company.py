from employeeClass import CreateEmployee

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

myCompany.addEmployee(CreateEmployee("Dwight", "Schrute", 95000))  # Dwight schrute is the top salesman! Of course he gets paid more than his other salesman!
myCompany.addEmployee(CreateEmployee("Stanley", "Hudson", 85000))
myCompany.addEmployee(CreateEmployee("Jim", "Halpert", 85000))
myCompany.addEmployee(CreateEmployee("Michael", "Scott", 120000))
myCompany.addEmployee(CreateEmployee("David", "Wallace", 500000))

print(myCompany.Employees)

# Print all the company employees
for i in myCompany.Employees:
    print(i.firstName, i.lastName)

print("I want to pay my peeps!")
myCompany.payEmployees()



