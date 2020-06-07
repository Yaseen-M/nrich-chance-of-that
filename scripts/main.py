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
                option = int(input('\nOption (1-3): '))
            except ValueError:
                print('Please enter a valid number.')
                continue

            if option == 1:
                x, y, tries = ListGen.gen_zero_r()
                print('List x: {}'.format(x))
                print('List y: {}'.format(y))
                print('Number of tries: {}'.format(tries))
            elif option == 2:
                print('In progress!')
            elif option == 3:
                exit_program = True


if __name__ == "__main__":
    menu = Menu()
