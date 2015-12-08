class Dog:
	def __init__(self, name, age, speaks):
		self.name = name 
		self.age = age
		self.speaks = speaks
		
	def getName(self):
		return self.name 
		
	def speaksSound(self):
		return self.speaks 
		
	def changeSpeak(self, speakNew):
		self.speaks = speakNew
		
		
lleo = Dog("Lleo", 7, "Bhow Bhow")
bob = Dog("Bob", 5, "Wurff")
print("Before meeting Bob, Lleo speaks : ")
print(lleo.speaksSound())
lleo.changeSpeak(bob.speaksSound()) 
print("Now Lleo speaks : ")
print(lleo.speaksSound())
