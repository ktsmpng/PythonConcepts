#Inheritance/ Polymorphism

"""Inheritance is the concept of inheriting FEATURES from ANOTHER CLASS. 
This can be applied when 'TWO OR MORE CLASSES SHARE COMMON ATTRIBUTES OR METHODS.' 

Base/ Super Class - the class that is inherited from.
Subclass - inherits from the base class.
Note: You can also have subclass of a subclass etc.. """

class Pet: #Create a Base Class

	def __init__(self, name, age): #Define initialization method
		self.name = name
		self.age = age

class Cat(Pet): #Creating a Cat class which inherits from Base Class "Pet" 

	def __init__(self, name, age):
		super().__init__(name, age) #Calling the SUper class in this case Pet and running its method like this"

def Main():

		thePet = Pet("Pet", 2)
		Garfield = Cat("Garfield", 4)

		print("Is Garfield a Cat? " + str(isinstance(Garfield, Cat))) #Returns True as Garfield is an instance of Cat 
		print("Is Garfield a Pet? " + str(isinstance(Garfield, Pet))) #Returns True as Garfield is a SUBCLASS of Pet
		print("Is thePet a Cat? " + str(isinstance(thePet, Cat))) #Returns False as thePet DOES NOT INHERIT FROM CAT!!
		print("Is thePet a Pet? " + str(isinstance(thePet, Pet))) #Returns True as thePet is an instance of pet

		print(Garfield.name) #Returns the name of Garfield from The Cat class which is inheriting from the Super class Pet!!

Main()

