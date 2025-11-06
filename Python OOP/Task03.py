class Animal:
    def speak(self):
        return "Animal Sounds"
    
class Dog(Animal):
    def speak(self):
        return ("woo")

class Cat(Animal):
    def speak(self):
        return ("mewo")
    
animal = [Dog(), Cat(), Animal()]

for animal in animal:
    print (animal.speak())