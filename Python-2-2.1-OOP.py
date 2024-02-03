car_count = 0 
def calculate_car_count():
    print("calculated")

class Car:
    manufacturer = "temp"
    def __init__(self, chassi_number, model="temp-model"):
        self.chassi_number = chassi_number
        self.model = model

    def run (self):
        print("run")

# Car.manufacturer = "toyota"       

# c1 = Car("11_MD")
# print(c1.chassi_number, c1.manufacturer, c1.model)
# c1.manufacturer = "nissan"
# c1.run()
# print(c1.chassi_number, c1.manufacturer, c1.model)
# Car.manufacturer = "bmw"
# print(c1.chassi_number, c1.manufacturer, c1.model)

# c2 = Car("11-AD", "Corolla")
# c2.run()
# print(c2.chassi_number, c2.manufacturer, c2.model)

car1 = Car(chassi_number="11-A5")
Car.manufacturer = "toyota" 
print(car1.chassi_number, car1.manufacturer, car1.model)



