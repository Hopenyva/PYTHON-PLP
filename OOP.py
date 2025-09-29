#Defining a class
class Cloth:
    def __init__(self , color, material):
        self.color = color
        self.material = material
class Dress(Cloth):
    pass
dress = Dress("lilac" , "silk")

print(dress.color)
print(dress.material)

#Enscapulation
class Cloth:
    def __init__(self):
        self.__dress = 5
    def take_dress(self):
        if self.__dress > 0:
            self.__dress -= 1
            print("One dress taken") 
        else:
            print("No dress left" )
cloth = Cloth()
cloth.take_dress()

#Polymorphism challenge

class Ferry:
    def path(self):
        return "Water"
class Bicycle:
    def path(self):
        return "road"
class Airplane:
    def path(self):
        return "air"
for vessel in [Ferry(), Bicycle(), Airplane()]:
    print(vessel.path())




