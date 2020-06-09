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
            ID = Menu.ask_for_data()
            Writer = streaming.Writer()
            Writer.verify_id_search(ID)
            
        elif option == 3:
            Title = Menu.ask_for_data()
            Writer = streaming.Writer()
            search_dic = Writer.verify_title_search(Title)

            if search_dic != None:
                array = Menu.search_results_adjust(search_dic)
                Menu.display_search_results_title(array)          

        elif option == 4:
            Genre = Menu.ask_for_data()
            Writer = streaming.Writer()
            search_dic = Writer.verify_genre_search(Genre)

            if search_dic != None:
                array = Menu.search_results_adjust(search_dic)
                Menu.display_search_results_general(array)          

        elif option == 5:
            Writer = streaming.Writer()
            working_dic, __ = Writer.file_processing()
            array = Menu.search_results_adjust(working_dic)
            Menu.display_search_results_general(array)    

        elif option == 6:
            Lists = streaming.Lists()
            search_dic = Lists.general("P",9)
            array = Menu.search_results_adjust(search_dic)
            Menu.display_search_results_movies(array)

        elif option == 7:
            Lists = streaming.Lists()
            search_dic = Lists.general("S",9)
            array = Menu.search_results_adjust(search_dic)
            Menu.display_search_results_series(array)

        elif option == 8:
            Lists = streaming.Lists()
            search_dic = Lists.general("D\n",9)
            array = Menu.search_results_adjust(search_dic)
            Menu.display_search_results_general(array)

        elif option == 9:
            upper,lower = Menu.ask_for_input_rating()
            Lists = streaming.Lists()
            search_dic = Lists.general("R\n",2, upper, lower)
            array = Menu.search_results_adjust(search_dic)
            Menu.display_search_results_general(array)

        elif option == 10:
            print("Exiting program...")
            quit()

