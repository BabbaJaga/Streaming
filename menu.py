import pandas

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

    def ask_for_input_rating(self):

        try:

            lower = float(input("Please give the lower rating limit: "))
            upper = float(input("Please give the upper rating limit: "))

            lst = range(1,6)

            while (lower not in lst or upper not in lst or lower > upper):
                print("Rating format not accepted, your rating interval can only be from 1 to 5 stars")
                lower = float(input("Please give the lower rating limit: "))
                upper = float(input("Please give the upper rating limit: "))
            
            return upper, lower

        except:

            print("Only integers are accepted!")
            return None, None

    def ask_for_input_menu(self):

        try:
            option = int(input("Please choose the desired option: "))
            return option

        except:
            print("Text is not allowed!")

    def ask_for_data(self):

        data = str(input("Enter your query: "))
        data = data.upper()
        return data

    def search_results_adjust(self,search_dic):

        if search_dic != None:
            array = pandas.DataFrame(data=search_dic.values(), columns = ["TITLE:", "DURATION:", "RATING:", "GENRE:", "AUDIENCE:", "SEASON:", "EPISODE:", "EPISODE TITLE:", "THEME:","ID:"])
            name = "ID:"
            removed = array.pop(name)
            array.insert(0, name, removed)
            array.replace(to_replace=[r"\t|\n|\r"], value=[""], regex=True, inplace=True)
            return(array)

        else:
            return "Not found"


    def display_search_results_title(self, array):

        if type(array) != "<class 'pandas.core.frame.DataFrame'>":

            #movie
            if array.iloc[0,6] == "":
                    print(array.iloc[:,0:6])
            #series
            elif array.iloc[0,9] == "":
                    print(array.iloc[:,0:9])
            #documentary
            else:
                    print(array)

        else:
            pass
    def display_search_results_general(self, array):

        if type(array) != "<class 'pandas.core.frame.DataFrame'>":
            print(array)
        
        else:
            pass

    def display_search_results_movies(self, array):

        if type(array) != "<class 'pandas.core.frame.DataFrame'>":
            print(array.iloc[:,0:6])
        
        else:
            pass

    def display_search_results_series(self, array):

        if type(array) != "<class 'pandas.core.frame.DataFrame'>":
            print(array.iloc[:,0:9])

        else:
            pass
        
