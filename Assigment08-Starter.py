# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <David Jamieson,<8/25/20>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'C:\_PythonClass\Assignment08\products.txt'
lstOfProductObjects = []
strChoice = ""  # string to identify used input [1 to 3]


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <David Jamieson>,<8/29/20>,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class

    product_name = ""
    product_price = 0.00

# Processing  ------------------------------------------------------------- #


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        file = open(file_name, "r")
        for line in file:
            name, price = line.split(",")
            row = [name.strip(), price.strip()]
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    # TODO: Add Code to process data to a file

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        product_file = open(file_name, "w")
        for row in list_of_product_objects:
            product_file.write(str(row[0]) + "," + str(row[1]) + "\n")
        product_file.close()
        print("Table  saved to file, ", file_name)
        return file_name, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """
    Processes visualizations from and to the user (input / output)

    properties:
        print_menu_tasks: function to print a list of menu tasks that the user can select
        input_menu_choice: function to prompt the user for input on their menu choice
        show_current_file_data: function to display the current list that they have created
        input_new_product: function to add a new product name and price to the list
    methods:
    changelog: (When,Who,What)
        <David Jamieson>,<8/29/20>,Modified code to complete assignment 8

    """

    # TODO: Add code to show menu to user

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) See current data in product file
        2) Add a new product (name and price) to the file
        3) Save changes and exit Program
        ''')

    # TODO: Add code to get user's choice

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user

    @staticmethod
    def show_current_file_data(list_of_rows):
        """ Shows the current list of products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current list of products are: *******")
        for row in list_of_rows:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user

    @staticmethod
    def input_new_product():
        name = str(input("Please enter a new product NAME: "))
        price = str(input("Please enter a PRICE for your product: "))
        return name, price

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

    # Load data from file into a list of product objects when script starts
    FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)


while True:

    # Show user a menu of options
    IO.print_menu_tasks()

    # Get user's menu option choice
    strChoice = IO.input_menu_choice()

    if strChoice.strip() == '1':  # Show user current data in the list of product objects
        IO.show_current_file_data(lstOfProductObjects)
        continue
    elif strChoice.strip() == '2':  # Let user add data to the list of product objects
        Product.product_name, Product.product_price = IO.input_new_product()
        lstRow = [Product.product_name, Product.product_price]
        lstOfProductObjects.append(lstRow)
        continue
    elif strChoice.strip() == '3':  # let user save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print('File saved - exiting program, thank you!')
        break
    else:  # prompt the user for the correct input type if they enter an input not between 1 to 3
        print('That is not an accepted input, please enter a number between [1 to 3]')
        continue


