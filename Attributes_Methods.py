# oop_classes_demo.py
"""
This script demonstrates:
1. Movie class
2. TemperatureConverter class
3. ShoppingItem class
"""

# ----------------------------
# 1. TemperatureConverter Class
# ----------------------------
class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15


# ----------------------------
# 2. ShoppingItem Class
# ----------------------------
class ShoppingItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


# ✅ Example : Instance Attributes & Method

# ----------------------------
# 3. Movie Class
# ----------------------------
class Movie:
    category = "Entertainment"  # class attribute

    def __init__(self, title, genre, rating):
        self.title = title # instance attribute
        self.genre = genre # instance attribute
        self.rating = rating # instance attribute

    def display_info(self):
        print(f"🎬 Movie: {self.title}\n   Genre: {self.genre}\n   Rating: {self.rating}/10\n")

# ----------------------------
# Demo / Test Cases / Multiple Methods
# ----------------------------
if __name__ == "__main__":
    # Movie Example
    movie1 = Movie("Inception", "Sci-Fi", 8.8)
    movie1.display_info()
    print(movie1.category) # Entertainment

    # TemperatureConverter Example
    temp = TemperatureConverter(25)
    print(f"🌡️ {temp.celsius}°C = {temp.to_fahrenheit()}°F")
    print(f"🌡️ {temp.celsius}°C = {temp.to_kelvin()}K\n")

    # ShoppingItem Example
    item1 = ShoppingItem("Laptop", 50000, 2)
    print(f"🛒 {item1.name} | Qty: {item1.quantity} | Total Price: ₹{item1.total_price()}")
