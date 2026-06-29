# private_attributes_demo.py

class Car:
    def __init__(self):
        self.__speed = 0   # private attribute

    def accelerate(self, value):
        self.__speed += value
        print(f"🚗 Accelerated! Current speed: {self.__speed}")

    def brake(self, value):
        self.__speed = max(0, self.__speed - value)
        print(f"🛑 Braked! Current speed: {self.__speed}")

    def get_speed(self):
        return self.__speed


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private attribute

    def get_marks(self):
        return self.__marks


if __name__ == "__main__":
    # Car Example
    car = Car()
    car.accelerate(30)
    car.brake(10)
    print("✅ Speed via getter:", car.get_speed())

    # Trying to access private variable directly
    try:
        print("❌ Direct access speed:", car.__speed)
    except AttributeError as e:
        print("⚠️ Error when accessing __speed directly:", e)

    # Student Example
    student = Student("Alice", 95)
    print("✅ Marks via getter:", student.get_marks())

    # Trying to access private variable directly
    try:
        print("❌ Direct access marks:", student.__marks)
    except AttributeError as e:
        print("⚠️ Error when accessing __marks directly:", e)

    # However, Python name mangling allows access like this (not recommended):
    print("🔎 Accessing private speed via _Car__speed:", car._Car__speed)
    print("🔎 Accessing private marks via _Student__marks:", student._Student__marks)

# Encapsulation relies on developer discipline, not strict compiler rules.