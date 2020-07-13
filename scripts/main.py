from list_gen import ListGen


class Menu():
    # Creates menu system
    def __init__(self):
        self.start_again = True
        while self.start_again:
            self.show_menu()

    # Shows menu
    def show_menu(self):
        print('\n-------------')
        print('Main menu')
        print('-------------')
        print('1) Generate two lists with zero correlation')
        print('2) Close program')

        try:
            option = int(input('\nOption (1 or 2): '))
            if option == 1:
                x, y, tries = ListGen.gen_zero_r()
                # Prints two lists and number of tries
                self.print_results(x, y, tries)
            elif option == 2:
                # Exits main menu
                self.start_again = False
            else:
                raise ValueError
        except ValueError:
            # Prints error message
            print('You entered an invalid option.')

    def print_results(self, x, y, tries):
        # Prints list x and y
        print('\nList x: {}'.format(', '.join(str(num) for num in x)))
        print('List y: {}'.format(', '.join(str(num) for num in y)))
        # Prints number of tries
        print('Number of tries: {}'.format(tries))


if __name__ == "__main__":
    menu = Menu()
