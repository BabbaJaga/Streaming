class Menu:
    def display_menu(self):

            print("*"*34)
            print("************ MAIN MENU ***********")
            print("*"*34)
            print("** 1. Add Videos                **")
            print("** 2. Check Video by ID         **")
            print("*"*34)
            print("************  REPORTS  ***********")
            print("*"*34)
            print("** 3. Search Video by Title     **")
            print("** 4. Search Video by Genre     **")
            print("** 5. Complete Video List       **")
            print("** 6. Movie List                **")
            print("** 7. Series List               **")
            print("** 8. Documentaries List        **")
            print("** 9. Rating List               **")
            print("**10. Exit                      **")
            print("*"*34)

    def ask_for_input_menu(self):

            option = int(input("Please choose the desired option: "))
            return option

    def ask_for_ID(self):

        ID = str(input("Enter Id   : "))
        ID = ID.upper()
        return ID