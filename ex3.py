class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._voltage = 12  # Chú ý thuộc tính voltage có dấu gạch chân, quy ước đây là internal property

    # Định nghĩa getter function
    @property
    def voltage(self):
        return self._voltage

    # Định nghĩa setter function
    @voltage.setter
    def voltage(self, volts):
        if volts > 230:
            raise ValueError("Voltage greater than 230 is dangerous")
        self._voltage = volts

    # Xử lý xóa thuộc tính
    @voltage.deleter
    def voltage(self):
        print("Warning: the radio will stop working!")
        del self._voltage


my_car = Car("yellow", "beetle", 1969)
print(f"My car uses {my_car.voltage} volts")

del my_car.voltage
my_car.voltage = 240