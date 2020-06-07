import menu
import streaming

if __name__ == "__main__":
    Menu = menu.Menu() 
    

    while True:

        Menu.display_menu()
        option = Menu.ask_for_input_menu()

        if option == 1:
            Writer = streaming.Writer()
            Writer.get_data()
            Writer.data_adjust()
            result, lst = Writer.verify_id_full()

            if result != "Failed":
                Writer.verify_writing(lst)

        elif option == 2:
            ID = Menu.ask_for_ID()
            Writer = streaming.Writer()
            Writer.verify_id_search(ID)
            
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            pass
        elif option == 10:
            pass

