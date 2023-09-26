

class Vehicle:
	def __init__(self,model_name, max_speed, mileage):
		
		self.model_name = model_name
		self.max_speed = max_speed
		self.mileage = mileage

	def seating_capacity(self, capacity):
		return f"The seating capacity of {self.model_name} is {capacity} passengers."
	

model_x = Vehicle('Model_x',200, 55)

print(f"Model Name: {model_x.model_name}\nMax speed: {model_x.max_speed}\nMileage : {model_x.mileage}\n\n")

car2 = Vehicle('Model_y',200, 55)

print(f"Model Name: {car2.model_name}\nMax speed: {car2.max_speed}\nMileage : {car2.mileage}\n\n")

model_x = Vehicle('Model_c',250, 45)

print(f"Model Name: {model_x.model_name}\nMax speed: {model_x.max_speed}\nMileage : {model_x.mileage}\n\n")



class Bus(Vehicle):
	pass


bus = Bus('Volvo - a bus',150,35)

print(f"Bus Model Name: {bus.model_name}\nMax Speed: {bus.max_speed}\nMileage: {bus.mileage}\n\n")

print(bus.seating_capacity(50))