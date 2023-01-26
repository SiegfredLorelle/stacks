import string
import sys

class Stack:
    def __init__(self, *elements):
        self.stack = [element for element in elements]
    
    def size(self):
        return len(self.stack)

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        
    def display(self):
        if self.is_empty():
            print("\nThe stacks seems to be empty.")
            return
        # Display the elements of the stack (The stack is reversed so that the element on top will be printed first)
        print("\nContents of the Stack:  ")
        [print(f"|          {data}          |") for data in list(reversed(self.stack))]




class App:

    # Maps operator with its level in order of operations (higher means first)
    operators = {
        "^": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1
    }
    operands = string.ascii_letters + string.digits


    def __init__(self):
        self.main_menu()

    def main_menu(self):
        print("\n**********   Infix to Postfix Conversion   **********")

        print("NOTE: each character of an operand is considered to be")

        infix = self.ask_for_infix()
        
        postfix = self.convert_to_postfix(infix)

        print(postfix)

        buffer()

        self.main_menu()

    def ask_for_infix(self):
            number_of_unclosed_parenthesis = 0
            
            infix = input("\nEnter the infix expression:  ").replace(" ", "")
            for character in infix:
                if character == "(":
                    number_of_unclosed_parenthesis += 1
                elif character == ")":
                    number_of_unclosed_parenthesis -= 1
                    if number_of_unclosed_parenthesis < 0:
                        print("Cannot read infix expression. Probably a problem with your parenthesis.")
                        return self.ask_for_infix()
                elif not (character in App.operands or character in App.operators):
                    print(f"'{character}' is invalid.")
                    return self.ask_for_infix()
            if number_of_unclosed_parenthesis != 0:
                print("Cannot read infix expression. Probably a problem with your parenthesis.")
                return self.ask_for_infix()
            return infix


    def convert_to_postfix(self, infix):
        operator_stack = Stack()
        postfix_stack = Stack()

        for character in infix:

            if character in App.operands:
                postfix_stack.push(character)

            elif character == "(":
                operator_stack.push(character)

            elif character == ")":
                while (not operator_stack.is_empty() and operator_stack.peak() != "("):
                    postfix_stack.push(operator_stack.pop())
                operator_stack.pop()

            else:
                while (not operator_stack.is_empty() and operator_stack.peak() != "(" and App.operators[operator_stack.peak()] >= App.operators[character]):
                        postfix_stack.push(operator_stack.pop())
                operator_stack.push(character)

        while not operator_stack.is_empty():
            postfix_stack.push(operator_stack.pop())

        return " ".join(postfix_stack.stack)







# HELPER FUNCTIONS ------------------------------------------------------------------------

def buffer():
    """ Asks for any input, acts as a buffer to give enough time for the user to read """
    input("\nPress any key to proceed:  ")

# END OF HELPER FUNCTIONS -----------------------------------------------------------------


if __name__ == "__main__":
    App()



# TODO
# COMMENTS, TESTING, CATCH ERRORS LIKE INCOMPLETE PARENTHESIS, OR
