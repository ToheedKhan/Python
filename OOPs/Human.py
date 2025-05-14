
# class Human():
# OR
class Human:
    #class variables
    database = []
    population = 0
    id_seq = 101

    #constructor
    def __init__(self, name, age, is_alive=True):
        #instance variables
        self.name = name
        self.age = age
        self.is_alive = is_alive

        #adding id of an object
        self.id = Human.id_seq
        Human.id_seq += 1

        Human.population += 1

        #adding object to the database
        Human.database.append(self)

# instance method
    def instroduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        print("I am a human.")

    def die(self):
        
        if self.is_alive:
           print(self.name, "is dying")
           self.is_alive = False
           Human.population -= 1
        else:
            print("{} is already dead".format(self.name))
            print(f"{self.name} is already dead")

#magic functions
    def __repr__(self):
        return f"Human({self.name}, {self.age}, {self.is_alive})"
    
class Hitman(Human):
    def __init__(self, name, age, is_alive=True):
        super().__init__(name, age, is_alive)
        
        #additional Hitman properties
        self.kills = 0
        self.kills_list = []

    def kill(self, person):
        """Person will be an obj of Human class"""
        
        if self.is_alive:
            print(f"{self.name} killed {person.name}")
            self.kills += 1
            self.kills_list.append(person)
            person.die()
        else:
            print(f"{self.name} is dead and cannot kill anyone.")
    
h1 = Human("John", 25)
h1.instroduce()
h2 = Human("Jane", 30)
h2.instroduce()

print(Human.database)
print(f"Population: {Human.population}")

print(Human.database[-1].name)

print(h1.is_alive)

h1.die()
print(h1.is_alive)
h1.die()

print(Human.database)
print(h1)


# Creating Hitman instance
h3 = Hitman("James", 35)
h3.instroduce()
print(h3.database)
print(f"Population: {Hitman.population}")
print(h3.__repr__)