# employee_manager_inheritance.py

# Example : Simple Inheritance

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call parent constructor
        super().__init__(name, salary)
        self.department = department

    # Method overriding
    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"
    
# Python does not support method overloading by argument count like some languages. Instead, use default values or *args.
# Another example below with Calculator class

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))        # 2
print(calc.add(2, 3))     # 5
print(calc.add(2, 3, 4))  # 9


if __name__ == "__main__":
    emp = Employee("Alice", 50000)
    mgr = Manager("Bob", 80000, "IT")

    print(emp.get_details())   # Employee: Alice, Salary: 50000
    print(mgr.get_details())   # Manager: Bob, Salary: 80000, Department: IT
