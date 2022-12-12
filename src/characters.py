
class Character():
    def __init__(self, name, movements, hits, specials):
        self.name = name
        self.movements = movements
        self.hits = hits
        self.specials = specials
        self.energy = 6
        self.is_alive = True
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)