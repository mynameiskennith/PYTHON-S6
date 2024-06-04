class person:
    __species = 'Homo Sapiens'

    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def get_species(self):
        return self.__species

a = person('Ken',34,50)
print(a.get_species()) 
a.species='hhh'
print(a.get_species()) 
 