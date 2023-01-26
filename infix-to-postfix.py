import sys

class Stack:
    def __init__(self, *elements):
        self.stack = [element for element in elements]
    
    def size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peak(self):
        return self.stack[len(self.stack)]
        
    def display(self):
        if self.size() == 0:
            print("\nThe stacks seems to be empty.")
            return

        # Display the elements of the stack (The stack is reversed so that the element on top will be printed first)
        print("\nContents of the Stack:  ")
        [print(f"|          {data}          |") for data in list(reversed(self.stack))]




class App:

    # Class variable of keys mapping to choices
    choice_keys = {
        1: "Push",
        2: "Pop",
        3: "Display Stack",
        4: "Exit"
    }

    def __init__(self):
        self.stack = Stack()
        self.main_menu()

    def main_menu(self):
        print("\n**********   Infix to Postfix Conversion   **********\n")

        self.ask_for_infix()
        
        self.convert_to_postfix()

        buffer()

        self.main_menu()
        
    def ask_for_infix(self):
        ...
    
    def convert_to_postfix(self):
        ...
    









# HELPER FUNCTIONS ------------------------------------------------------------------------

def ask_for_int(message):
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


if __name__ == "__main__":
    App()



# TODO
# COMMENTS, TESTING
