#Inheritance/ Polymorphism

"""	Inheritance is the concept of inheriting FEATURES from ANOTHER CLASS. 
	This can be applied when 'TWO OR MORE CLASSES SHARE COMMON ATTRIBUTES OR METHODS.' 

	Base/ Super Class - the class that is inherited from.
	Subclass - inherits from the base class.
	Note: You can also have subclass of a subclass etc.. """

"""	Polymorphism is concept of defining a method in a Base class
	which is then OVERIDED BY THE SUBCLASSES!
	Each subclass will have a DIFFERENT IMPLEMENTATION OF THIS METHOD. 
	When the super class method is called,
	it will choose which method to run depending on the subclass."""

class Pet: #Create a Base Class

	def __init__(self, name, age): #Defining initialization method
		self.name = name
		self.age = age

	def talk(self):
		raise NotImplementedError("Subclass must implement Talk Method")

class Cat(Pet): #Creating a Cat class which inherits from Base Class "Pet" 

	def __init__(self, name, age):
		super().__init__(name, age) #Calling the Super class in this case Pet and running its method like this"

	def talk(self): 
		return "Meow" 

class Dog(Pet):

	def __init__(self, name, age):
		super().__init__(name, age)

	def talk(self):
		return "Woof"

def Main():

		pets = [Cat("Garfield", 4), Dog("Bruno", 3), Cat("Kitty", 3)] #Creating a list of Pets

		for pet in pets: #Running a for loop to print out each pets attributes and method. 
			print("Name: " + pet.name + ", Age: " + str(pet.age) + ", Says: " + pet.talk())

Main()
