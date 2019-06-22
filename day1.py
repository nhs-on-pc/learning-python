import datetime

class Person(object):     # Định nghĩa một class
    species = "Homo Sapiens"  # Định nghĩa một thuộc tính

    def __init__(self, name, birth_year):   # Constructor - hàm khởi tạo
        self.name = name
        self.birth_year = birth_year

    def __str__(self):          # overload special method __str__, method có trong mọi class
        return self.name

    def rename(self, renamed):
        self.name = renamed
        print("Now my name is {}".format(self.name))

    def speak(self, text):
        print(f"{self.name} says {text}")

    def age(self): int




kelly = Person("Kelly", 1920)
joseph = Person("Joseph", 1945)
john_doe = Person("John Doe", 1978)

print(kelly)


kelly.rename("Harris")
print(kelly)
print(kelly.species)
kelly.speak("hello world")

def age(self):
    

now = datetime.datetime.now()
return now.year - self.birth_year

print()

