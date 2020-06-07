from list_gen import ListGen


class Menu():
    def __init__(self):
        self.show_menu()

    def show_menu(self):
        exit_program = False
        while not exit_program:
            print('\n-------------')
            print('Main menu')
            print('-------------')
            print('1) Generate two lists with zero correlation')
            print('2) Generate probability of zero correlation')
            print('3) Close program')

            try:
                option = int(input('\nOption (1-3)): '))
            except ValueError:
                print('Please enter a valid number.')
                continue

            if option == 1:
                print(ListGen.gen_zero_r())
            elif option == 2:
                print('In progress!')
            elif option == 3:
                exit_program = True


menu = Menu()
