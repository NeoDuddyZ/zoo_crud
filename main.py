#need to be refactored
from animal import Animal

x = int()
animal_list = []
while(True):
    x = int(input('1-Create animal\n'
          '2-Read Animal\n'
          '3-Update Animal\n'
          '4-Delete Animal\n'
          '5-List Animals\n'
          '0-Exit\n'))
    if x == 1:
        name = str(input('Write the name of the animal: '))
        type = str(input('Write the type of the animal: '))
        new_animal = Animal(name, type)
        animal_list.append(new_animal)
    elif x == 2:
        index = int(input("Write the index of the animal: (if you don't know type -1 to see all animals with index)\n"))
        if index == -1 and len(animal_list) > 0:
            count = 0
            for i in animal_list:
                print(f'{count} - {i.show_animal()}')
                count += 1
        elif index != -1  and len(animal_list) > 0 and index < len(animal_list):
            print(animal_list[index].show_animal())
        else:
            pass
    elif x == 3:
        while(True):
            index = int(input("Write the index of the animal: (if you don't know type -1 to see all animals with index or -2 to exit)\n"))
            if index == -1 and len(animal_list) > 0:
                count = 0
                for i in animal_list:
                    print(f'{count} - {i.show_animal()}')
                    count += 1
            elif index == -2 and len(animal_list) > 0:
                break
            elif index >= 0 and len(animal_list) > 0 and index < len(animal_list):
                name = str(input('Write the new name of the animal: '))
                type = str(input('Write the new type of the animal: '))
                animal_list[index].update(name, type)
                break
            else:
                pass
    elif x == 4:
        while (True):
            index = int(input(
                "Write the index of the animal: (if you don't know type -1 to see all animals with index or -2 to exit)\n"))
            if index == -1 and len(animal_list) > 0:
                count = 0
                for i in animal_list:
                    print(f'{count} - {i.show_animal()}')
                    count += 1
            elif index == -2 and len(animal_list) > 0:
                break
            elif index >= 0 and len(animal_list) > 0 and index < len(animal_list):
                animal_list.pop(index)
                break
            else:
                pass
    elif x == 5:
        count = 0
        for i in animal_list:
            print(f'{count} - {i.show_animal()}')
            count += 1
    elif x == 0:
        break
    else:
        print('Invalid Value!\n')