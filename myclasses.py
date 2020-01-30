class Burger:
	def __init__(self):
		self.cost = 0
		self.pattyTypes = []
		self.numPatties = 0
		self.numCheeseSlices = 0
		self.withVeggies = False

	def addPatty(self, pattyType, quantity):
		if pattyType == "Angus":
			self.cost += 75 * quantity
			for i in range(0, quantity):
				self.pattyTypes.append("Angus")
			self.numPatties += quantity
		elif pattyType == "Wagyu":
			self.cost += 100 * quantity
			for i in range(0, quantity):
				self.pattyTypes.append("Wagyu")
			self.numPatties += quantity

	def addCheese(self, quantity):
		self.cost += quantity * 25
		self.numCheeseSlices += quantity

	def addVeggies(self):
		self.withVeggies = True

	def __str__(self):
		newStr = ''
		newStr += 'Burger Specs:'
		newStr += '\nPatty Types - '
		for item in self.pattyTypes:
			newStr += '\n' + item
		newStr += '\nNumber of Patties: ' + str(self.numPatties)
		newStr += '\nNumber of Cheese Slices: ' + str(self.numCheeseSlices)
		if self.withVeggies: 
			newStr += '\nWith Veggies'
		newStr += '\nPHP ' + str(self.cost)
		return(newStr)


