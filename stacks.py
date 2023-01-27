import sys

class Stack:
    """ Linear data structure following Last In First Out Principle (LIFO), top of the stack is the only accessible element """

    def __init__(self, *elements):
        """ Stack is represented as a list, the top of the stack is the last element of the list """
        self.stack = [element for element in elements]

    def size(self):
        """ Returns the number of elements in the stack """
        return len(self.stack)

    def is_empty(self):
        """ Returns true if stack is empty, else return false """
        if self.size() == 0:
            return True
        return False

    def push(self, data: int):
        """ Accepts a data of type int, push it a the top of the stack """
        self.stack.append(data)

    def pop(self):
        """ Deletes the element at the top of the stack """
        # Pop function without arguments, pops/deletes the last element of the list
        return self.stack.pop()

    def peak(self):
        """ Returns the element at the top of the stack """
        # -1 index is the last element of the list
        return self.stack[-1]

    def display(self):
        """ Displays the elements of the stack if it is not empty """
        # If stack is empty, simply inform user about it
        if self.is_empty():
            print("\nThe stacks seems to be empty.")
            return

        # Display the elements of the stack (The stack is reversed so that the element on top will be printed first)
        print("\nContents of the Stack:  ")
        [print(f"|          {data}          |") for data in list(reversed(self.stack))]




class App:
    """ Holds the stack, manages communication between user and program """

    # Class variable of input keys mapped to what the choice does
    choice_keys = {
        1: "Push",
        2: "Pop",
        3: "Display Stack",
        4: "Exit"
    }

    def __init__(self):
        """ Create a stack, and launch the main menu immediately as soon as the app is initialized """
        self.stack = Stack()
        self.main_menu()

    def main_menu(self):
        """ Show the choices to operate the stack """

        print("\n"
            "*******************************************\n"
            "**********   Main Menu           **********\n"
            "**********   [1] Push            **********\n"
            "**********   [2] Pop             **********\n"
            "**********   [3] Display Stack   **********\n"
            "**********   [4] Exit            **********\n"
            "*******************************************"
        )

        # Asks the user to choose from the possible choices
        choice = self.ask_for_choice()
        # Execute operation based on user's choice
        self.choice_manager(choice)
        # Acts a buffer to give enough time for the user to read
        buffer()

        # After the operation, redirect to main menu
        return self.main_menu()


    def ask_for_choice(self):
        """ Prompt for a choice """
        # Keep on prompting until a valid choice is chosen
        while True:
            choice = ask_for_int(("\nEnter number of your choice:  "))
            if choice in App.choice_keys:
                return App.choice_keys[choice]
            print("Choice must be 1-4 inclusive.")


    def choice_manager(self, choice):
        """ Execute operations based on choice """

        match choice:
            # If chosen operation is push, then ask for a data to push on top of the stack, then push it, then display the stack
            case "Push":
                data = ask_for_int("\nEnter data/value to push:  ")
                print(f"\nElement '{data}' is pushed on to the stack.")
                self.stack.push(data)
                self.stack.display()

            # If chosen operation is pop, then try popping the element on top of the stack, if stack has no elements, then inform user about it
            case "Pop":
                try:
                    print(f"\nElement '{self.stack.pop()}' is popped out of the stack.")
                    if self.stack.size() != 0:
                        self.stack.display()
                except IndexError:
                    print("\nStack seems to be empty. NOTHING was popped.")

            # If chosen operation is display, then display the elements in the stack
            case "Display Stack":
                self.stack.display()

            # If chosen operation is exit, then close the app
            case "Exit":
                sys.exit("\nClosing the program ...\n")





# HELPER FUNCTIONS ------------------------------------------------------------------------
# Helper functions are usually in a separate py file, 
# However, since OnlineGDB can only run the main file, helper functions must stays here

def ask_for_int(message):
    """ Keep on asking for an int, until a valid one is given """
    while True:
        try:
            given_int = int(input(message))
            return given_int
        except ValueError:
            print("Input must be an integer.")


def buffer():
    """ Asks for any input, acts as a buffer to give enough time for the user to read """
    input("\nPress any key to proceed:  ")

# END OF HELPER FUNCTIONS -----------------------------------------------------------------



# Launches the app
if __name__ == "__main__":
    App()
