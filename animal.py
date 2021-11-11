class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_animal(self):
        return (f'{self.name} is a(n) {self.species}')

    def get_type(self):
        return self.species

    def get_name(self):
        return self.name

    def set_type(self, species):
        self.species = species

    def set_name(self, name):
        self.name = name

    def update(self, name, species):
        print(f'{self.name} was changed to {name}\n{self.species} was changed to {species}')
        self.set_name(name)
        self.set_type(species)
