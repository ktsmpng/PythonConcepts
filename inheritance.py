#Inheritance/ Polymorphism

"""Inheritance is the concept of inheriting FEATURES from ANOTHER CLASS. 
This can be applied when 'TWO OR MORE CLASSES SHARE COMMON ATTRIBUTES OR METHODS.' 

Base/ Super Class - the class that is inherited from.
Subclass - in herits from the base class.
Note: You can also have subclass of a subclass etc.. """

class Pet: #Create a Base Class

	def __init__(self, name, age): #Define initialization method
		self.name = name
		self.age = age

class Cat(Pet): #Creating a Cat class which inherits from Base Class "Pet" 

	def __init__(self, name, age):
		super().__init__(name, age) #Call SUper class in this case Pet and run its method like this"

def Main():

		thePet = Pet("Pet", 2)
		Garfield = Cat("Garfield", 4)

		print("Is Garfield a Cat?" + str(isinstance(Garfield, Cat)))
		print("Is Garfield a Pet?" + str(isinstance(Garfield, Pet)))
		print("Is thePet a Cat?" + str(isinstance(thePet, Cat)))
		print("Is thePet a Pet?" + str(isinstance(thePet, Pet)))

		print(Garfield.name)

Main()

