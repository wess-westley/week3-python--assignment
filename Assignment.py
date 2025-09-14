# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.__battery = battery  # Encapsulation: make battery private

    # Getter for battery
    def get_battery(self):
        return self.__battery

    # Method to display phone info
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage, Battery: {self.__battery}%"

    # Method to simulate charging
    def charge_battery(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.model} charged. Battery is now {self.__battery}%")

    # Method to simulate using battery
    def use_battery(self, amount):
        self.__battery = max(0, self.__battery - amount)
        print(f"{self.model} used. Battery is now {self.__battery}%")


# Subclass
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, android_version):
        super().__init__(brand, model, storage, battery)
        self.android_version = android_version

    # Polymorphism: override phone_info
    def phone_info(self):
        return f"{self.brand} {self.model} running Android {self.android_version}, Storage: {self.storage}GB, Battery: {self.get_battery()}%"

    # Extra method specific to Android
    def install_app(self, app_name):
        print(f"{app_name} has been installed on your {self.model}.")


# Create objects
my_phone = Smartphone("Apple", "iPhone 15", 256, 80)
print(my_phone.phone_info())
my_phone.charge_battery(15)
my_phone.use_battery(30)

print("")

my_android = AndroidPhone("Samsung", "Galaxy S23", 512, 50, "13")
print(my_android.phone_info())
my_android.install_app("Spotify")
my_android.charge_battery(40)
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses with polymorphism
class Car(Vehicle):
    def move(self):
        print(" Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print(" Sailing on the water...")

class Bike(Vehicle):
    def move(self):
        print(" Pedaling on the path...")

# Test polymorphism
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()
