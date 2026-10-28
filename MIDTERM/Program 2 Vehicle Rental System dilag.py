class Vehicle:
    def __init__(self, brand, daily_rate):
        self.brand = brand
        self.daily_rate = daily_rate

    def calculate_rental(self, days):
        total = self.daily_rate * days
        return total

class Car(Vehicle):
    def __init__(self, brand, daily_rate, seat_capacity):
        super().__init__(brand, daily_rate)
        self.seat_capacity = seat_capacity

    def show_details(self):
        print("Car:", self.brand, "| Daily rate: PHP", self.daily_rate, "| Seats:", self.seat_capacity)

class Motorcycle(Vehicle):
    def __init__(self, brand, daily_rate, engine_capacity_cc):
        super().__init__(brand, daily_rate)
        self.engine_capacity_cc = engine_capacity_cc

    def show_details(self):
        print("Motorcycle:", self.brand, "| Daily rate: PHP", self.daily_rate, "| Engine:", self.engine_capacity_cc, "cc")


my_car = Car("Toyota", 1500, 5)
my_motorcycle = Motorcycle("Honda", 500, 150)

days = 3

my_car.show_details()
car_price = my_car.calculate_rental(days)
print("Rental charge for 3 days: PHP", car_price)
print()

my_motorcycle.show_details()
bike_price = my_motorcycle.calculate_rental(days)
print("Rental charge for 3 days: PHP", bike_price)
print()
