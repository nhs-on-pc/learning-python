class Car:
   def __init__(self, manufacturer, model):
       self.manufacturer = manufacturer
       self.model = model

   def __str__(self):
       return f"{self.model} by {self.manufacturer}"

   def run(self):
       print("car runs")

   def stop(self):
       print("car stops")

fadil = Car("Honda", "Civic")
fadil.run()
fadil.stop()
print(fadil)

triton = Car("Mitsubishi", "Triton")
triton.run()
print(triton)