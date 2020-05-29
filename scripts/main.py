from list_generator import ListGenerator


class Menu():
    def __init__(self):
        self.show_menu()

    def show_menu(self):
        exit_program = False
        while not exit_program:
            print('\n-------------')
            print('Main menu')
            print('-------------')
            print('1) Generate two lists with no correlation')
            print('2) Generate probability of zero correlation')
            print('3) Close program')

            option = int(input('\nOption (1/2)): '))
            if option == 1:
                print(ListGenerator.generate_zero_r())
            elif option == 2:
                print('In progress!')
            elif option == 3:
                exit_program = True


menu = Menu()
