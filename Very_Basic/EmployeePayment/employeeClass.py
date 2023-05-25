
WEEKS_IN_YEAR = 52

# Utilize inheritance to create different types of paid employees

class CreateEmployee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


class CreateSalaryEmployee(CreateEmployee):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary = salary

    def calculatePaycheck(self):
        return self.salary / WEEKS_IN_YEAR

class CreateHourlyEmployee(CreateEmployee):
    def __init__(self, firstName, lastName, weeklyHours, hourlyRate):
        super().__init__(firstName, lastName)
        self.weeklyHours = weeklyHours
        self.hourlyRate = hourlyRate

    def calculatePaycheck(self):
        return self.weeklyHours * self.hourlyRate


class CreateCommissionEmployee(CreateSalaryEmployee):
    def __init__(self, firstName, lastName, salary, salesNumber, commissionRate):
        super().__init__(firstName, lastName, salary)
        self.salesNumber = salesNumber
        self.commissionRate = commissionRate

    def calculatePaycheck(self):
        regularSalary = super().calculatePaycheck()
        totalCommission = self.salesNumber * self.commissionRate
        return regularSalary + totalCommission

