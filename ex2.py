import csv

class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def __str__(self):
        return f'Car {self.color} : {self.model} : {self.year}'

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __add__(self, other):
        return Car(self.color + other.color,
                   self.model + other.model,
                   int(self.year) + int(other.year))


my_car = Car("yellow", "Beetle", "1966")
your_car = Car("red", "Corvette", "1967")

print(my_car < your_car)

print(my_car > your_car)

print(my_car == your_car)

print(my_car + your_car)
print("------------")
cars = [
    Car("yellow", "Beetle", "1966"),
    Car("black", "Toyota", "1954"),
    Car("white", "Mitsubishi", "1978"),
    Car("silver", "Ford Mustang", "1942"),
    Car("silver", "Ford Ranger", "1975")
]

cars.sort()

for car in cars:
    print(car)

with open('myfile.csv', 'w', newline='\n') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Header1', 'Header2', 'Header3'])
    csvwriter.writerow(cars)

