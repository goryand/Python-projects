
WEEKS_IN_YEAR = 52


class CreateEmployee:
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def calculatePaycheck(self):
        return self.salary / WEEKS_IN_YEAR

