import array as arr
import sys

class Stack:
    def __init__(self, *elements):
        self.stack = arr.array("l", elements)
        self.top = len(elements)
    
    def size(self):
        return self.top

    def push(self, data):
        self.top += 1
        self.stack.append(data)

    def pop(self):
        self.top -= 1
        return self.stack.pop()

    def peak(self):
        # [self.top - 1] can be replaced with [-1], both will return the last element of the array
        return self.stack[self.size() - 1]
        
    def display(self):
        # self.top can be replaced with len(self.stack), both returns the number of elements of the stack
        if self.size() == 0:
            print("\nThe stacks seems to be empty.")
            return

        # Display the elements of the stack (The stack is reversed so that the element on top will be printed first)
        print("\nContents of the Stack:  ")
        [print(f"|          {data}          |") for data in arr.array("l", reversed(self.stack))]




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
        print("\n"
            "*******************************************\n"
            "**********   Main Menu           **********\n"
            "**********   [1] Push            **********\n"
            "**********   [2] Pop             **********\n"
            "**********   [3] Display Stack   **********\n"
            "**********   [4] Exit            **********\n"
            "*******************************************"
        )

        self.choice_manager(self.ask_for_choice())

    def ask_for_choice(self):
            while True:
                choice = ask_for_int(("\nEnter number of your choice:  "))
                if choice in App.choice_keys:
                    return App.choice_keys[choice]
                print("Choice must be 1-4 inclusive.")



    def choice_manager(self, choice):
        match choice:
            case "Push":
                data = ask_for_int("\nEnter data/value to push:  ")
                print(f"\nElement '{data}' is pushed on to the stack.")
                self.stack.push(data)
                self.stack.display()

            case "Pop":
                try:
                    print(f"\nElement '{self.stack.pop()}' is popped out of the stack.")
                    if self.stack.size() != 0:
                        self.stack.display()
                except IndexError:
                    print("Stack seems to be empty. NOTHING was popped.")

            case "Display Stack":
                    self.stack.display()

            case "Exit":
                sys.exit("\nClosing the program ...\n")

        buffer()

        self.main_menu()






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


