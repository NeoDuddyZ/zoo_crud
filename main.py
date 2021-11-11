import crud_functions as crf

x = int()

while(True):
    try:
        x = int(input('\n1-Create animal\n'
          '2-Read Animal\n'
          '3-Update Animal\n'
          '4-Delete Animal\n'
          '5-List Animals\n'
          '0-Exit\n'))
        if x == 1:
            crf.create_animal()
        elif x == 2:
            crf.read_animal()
        elif x == 3:
            crf.update_animal()
        elif x == 4:
            crf.delete_animal()
        elif x == 5:
            crf.print_animal_list()
        elif x == 0:
            break
        else:
            print('Invalid Value!\n')
    except:
        print('invalid input')
        pass
