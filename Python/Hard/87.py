class Employee:
    company_funds = 100000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def request_fund(self, amount):
        if Employee.company_funds >= amount:
            Employee.company_funds -= amount
            self.salary += amount
        else:
            raise ValueError("Not enough funds in the company")

    def print_funds(self):  
        print(f"Company funds left: {Employee.company_funds}")

def main():
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 45000)

    try:
        emp1.request_fund(60000)
    except ValueError as e:
        print(f"Error for {emp1.name}: {e}")

    try:
        emp2.request_fund(30000)
    except ValueError as e:
        print(f"Error for {emp2.name}: {e}")

    emp1.print_funds()  

main()