class Employee:
    def __init__(self, name, age, salary):
        self.name = name      # triggers name setter
        self.age = age        # triggers age setter
        self.salary = salary  # triggers salary setter

    # -------------------------
    # Name Property
    # -------------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    # -------------------------
    # Age Property
    # -------------------------
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if value < 18:
            raise ValueError("Employee must be at least 18 years old.")
        self._age = value

    # -------------------------
    # Salary Property
    # -------------------------
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number.")
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value


emp = Employee("Alice", 25, 50000)

print(emp.name)
print(emp.age)
print(emp.salary)

emp.salary = 7000
print(emp.salary)
emp.salary = -1000
print(emp.salary)

emp.age = 12
print(emp.age)

emp.name = ""
print(emp.name)
