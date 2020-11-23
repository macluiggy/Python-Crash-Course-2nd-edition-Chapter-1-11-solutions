class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, manufacturer, model, year):
		"""Initialize attributes to describe the car."""
		self.manufacturer = manufacturer
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly dormatted descriptive name."""
		long_name = f"{self.year} {self.manufacturer} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		if miles > 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back the odometer!")

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describin the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range == 260
		elif self.battery_size == 100:
			range == 315

		print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, manufacturer, model, year):
		"""
		Initialize attributes of the parents class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(manufacturer, model, year)
		self.battery = Battery()

	

	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()