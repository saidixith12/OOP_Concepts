# dunder_methods_demo.py
"""
This script demonstrates:
1. __str__ with Movie class
2. __add__ with Time class
3. __len__ and __getitem__ with ShoppingList class
"""

# Example : __init__ and __str__

# ----------------------------
# 1. Movie with __str__
# ----------------------------
class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __str__(self):
        return f"{self.title} ({self.genre})"


# Example 2: __add__ for Operator Overloading

# ----------------------------
# 2. Time with __add__
# ----------------------------
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"


# Example : __init__ and __len__ & __getitem__


# ----------------------------
# 3. ShoppingList with __len__ & __getitem__
# ----------------------------
class ShoppingList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


# ----------------------------
# Demo / Test Cases
# ----------------------------
if __name__ == "__main__":
    # Movie Example
    movie = Movie("Inception", "Sci-Fi")
    print("🎬 Movie:", movie)   # Inception (Sci-Fi)

    # Time Example
    t1 = Time(2, 50)
    t2 = Time(1, 30)
    t3 = t1 + t2
    print("🕒 Time 1:", t1)
    print("🕒 Time 2:", t2)
    print("🕒 Sum:", t3)

    # ShoppingList Example
    shopping_list = ShoppingList(["Milk", "Bread", "Eggs"])
    print("🛒 Shopping List Length:", len(shopping_list))
    print("🛒 First Item:", shopping_list[0])
