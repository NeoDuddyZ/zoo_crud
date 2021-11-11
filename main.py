#need to be refactored
from animal import Animal
animal_list = []
x = int()


def create_animal():
    name = str(input('Write the name of the animal: '))
    type = str(input('Write the type of the animal: '))
    new_animal = Animal(name, type)
    animal_list.append(new_animal)

def set_new_animal(index):
    name = str(input('Write the new name of the animal: '))
    type = str(input('Write the new type of the animal: '))
    animal_list[index].update(name, type)

def read_animal():
    index = int(input("Write the index of the animal: (if you don't know type -1 to see all animals with index)\n"))
    if index == -1 and len(animal_list) > 0:
        print_animal_list()
    elif index != -1 and len(animal_list) > 0 and index < len(animal_list):
        print(animal_list[index].show_animal())
    else:
        pass

def update_animal():
    while(True):
        index = int(input("Write the index of the animal: (if you don't know type -1 to see all animals with index or -2 to exit)\n"))
        if index == -1 and len(animal_list) > 0:
            print_animal_list()
        elif index == -2 and len(animal_list) > 0:
            break
        elif index >= 0 and len(animal_list) > 0 and index < len(animal_list):
            set_new_animal(index)
            break
        else:
            pass

def print_animal_list():
        count = 0
        for i in animal_list:
            print(f'{count} - {i.show_animal()}')
            count += 1

def delete_animal():
    while (True):
            index = int(input(
                "Write the index of the animal: (if you don't know type -1 to see all animals with index or -2 to exit)\n"))
            if index == -1 and len(animal_list) > 0:
                print_animal_list()
            elif index == -2 and len(animal_list) > 0:
                break
            elif index >= 0 and len(animal_list) > 0 and index < len(animal_list):
                animal_list.pop(index)
                break
            else:
                pass


while(True):
    x = int(input('1-Create animal\n'
          '2-Read Animal\n'
          '3-Update Animal\n'
          '4-Delete Animal\n'
          '5-List Animals\n'
          '0-Exit\n'))
    if x == 1:
        create_animal()
    elif x == 2:
        read_animal()
    elif x == 3:
        update_animal()
    elif x == 4:
        delete_animal()
    elif x == 5:
        print_animal_list()
    elif x == 0:
        break
    else:
        print('Invalid Value!\n')