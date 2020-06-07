from list_gen import ListGen


class Menu():
    def __init__(self):
        self.start_again = True
        while self.start_again:
            self.show_menu()

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
                self.print_results(x, y, tries)
            elif option == 2:
                self.start_again = False
            else:
                raise ValueError
        except ValueError:
            print('You entered an invalid option.')

    def print_results(self, x, y, tries):
        print('\nList x: {}'.format(x))
        print('List y: {}'.format(y))
        print('Number of tries: {}'.format(tries))


if __name__ == "__main__":
    menu = Menu()
