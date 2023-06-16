
class Village:
    def __init__(self, name, country, populaiton):
        self.name = name
        self.country = country
        self.population=population

    def add_village_inhabitant(self,amount):
        self.amount=self.amount+amount

    def __str__(self):
        return f"{self.name} Village are in {self.country} and has {self.population} population"

class Building:
    def __init__(self,name, purpose, importance):
        self.name = name
        self.purpose = purpose
        self.importance = importance

    def priority(self, priority):
        self.priority = self.priority+priority


class GiftFactory(Building):
    gift = 0
    def __init__(self,name, purpose, importance, workers):
        super().__init__(self,name, purpose, importance)
        self.workers=workers
    def production(self,gift):
        self.gift = self.gift+gift
        
    

class SuntaHouse(Building):
    def __init__(self,name, purpose, importance, bedrooms):
        super().__init__(self,name, purpose, importance)
        self.bedrooms=bedrooms
    
class People:
    def __init__(self,first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name


class Sunta(People):
    def __str__(self):
        return f"HO HO HO"
        

class Workers(People):
    def __init__(self,first_name, last_name, productivity):
        super().__init__(self,first_name, last_name)
        self.productivity=productivity

class Animials:
    def __init__(self, name, age):    
        self.name = name
        self.age = age
    def __str__(self):   
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Reindeer(Animals):
    def speak(self,sound="reindeer noise"):
        return super().speak(sound)
    
    
