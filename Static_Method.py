# static_methods_demo.py

import math

class Geometry:
    @staticmethod
    def area_of_circle(radius):
        return math.pi * radius ** 2

    @staticmethod
    def area_of_square(side):
        return side * side


class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email


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

    # ✅ Static Utility Method: Format Car Model Name
    @staticmethod
    def format_model_name(name: str):
        """Utility method to format car model names properly"""
        return name.strip().title()


if __name__ == "__main__":
    # Geometry class usage
    print("📐 Area of Circle (r=5):", Geometry.area_of_circle(5))
    print("📐 Area of Square (side=4):", Geometry.area_of_square(4))

    # Validator usage
    print("📧 Is 'test@example.com' valid?", Validator.is_valid_email("test@example.com"))
    print("📧 Is 'invalidemail.com' valid?", Validator.is_valid_email("invalidemail.com"))

    # Car class usage with static method
    car = Car()
    car.accelerate(50)
    car.brake(20)
    print("✅ Current speed:", car.get_speed())

    model_name = "   tesla model 3   "
    print("🚘 Formatted Car Model Name:", Car.format_model_name(model_name))
