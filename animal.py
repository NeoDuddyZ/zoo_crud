class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def show_animal(self):
        return (f'{self.name} is a(n) {self.type}')

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def set_type(self, type):
        self.type = type

    def set_name(self, name):
        self.name = name

    def update(self, name, type):
        print(f'{self.name} was changed to {name}\n{self.type} was changed to {type}')
        self.set_name(name)
        self.set_type(type)
