from animal import Animal
animal_list = []

def create_animal():
    name = str(input('Write the name of the animal: '))
    species = str(input('Write the species of the animal: '))
    new_animal = Animal(name, species)
    animal_list.append(new_animal)

def set_new_animal(index):
    name = str(input('Write the new name of the animal: '))
    species = str(input('Write the new species of the animal: '))
    animal_list[index].update(name, species)

def read_animal():
    if(len(animal_list) > 0):
        while(True):
            index = int(input("Write the index of the animal: (if you don't know type -1 to see all animals with index  or -2 to exit)\n"))
            if index == -1 and len(animal_list) > 0:
                print_animal_list()
            elif index == -2:
                break
            elif index != -1 and index < len(animal_list):
                print(animal_list[index].show_animal())
            else:
                pass
    else:
        print('The list is void')

def update_animal():
    if(len(animal_list) > 0):
        while(True):
            index = int(input("Write the index of the animal: (if you don't know type -1 to see all animals with index or -2 to exit)\n"))
            if index == -1 and len(animal_list) > 0:
                print_animal_list()
            elif index == -2:
                break
            elif index >= 0 and index < len(animal_list):
                set_new_animal(index)
                break
            else:
                pass
    else:
        print('The list is void')

def print_animal_list():
    if(len(animal_list) > 0):
            count = 0
            for i in animal_list:
                print(f'{count} - {i.show_animal()}')
                count += 1
    else:
        print('The list is void')

def delete_animal():
    if(len(animal_list) > 0):
        while (True):
                index = int(input(
                    "Write the index of the animal: (if you don't know type -1 to see all animals with index or -2 to exit)\n"))
                if index == -1 and len(animal_list) > 0:
                    print_animal_list()
                elif index == -2:
                    break
                elif index >= 0 and  index < len(animal_list):
                    print(f'{animal_list[index].get_name()} was deleted')
                    animal_list.pop(index)
                    break
                else:
                    pass
    else:
        print('The list is void')
