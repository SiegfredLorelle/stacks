import string
import sys
import re

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
            return self.stack.pop()

    def peak(self):
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

        infix = self.ask_for_infix()
        
        postfix = self.convert_to_postfix(infix)

        print("\n"
            f"Postfix expression:  {postfix}"
        )

        self.try_again()


    def ask_for_infix(self):
            
            infix = input("\nEnter the infix expression:  ")

            infix = self.validate_infix(infix)

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

    def validate_infix(self, infix):
        number_of_unclosed_parenthesis = 0
        previous_character = ""
        has_operand = has_operator = False

        infix = re.sub("[\[{]", "(", infix)
        infix = re.sub("[]}]", ")", infix)
        infix = infix.replace(" ", "")


        for index, character in enumerate(infix):

            if character == "(":
                number_of_unclosed_parenthesis += 1
                previous_character = "parenthesis"
            elif character == ")":
                number_of_unclosed_parenthesis -= 1
                previous_character = "parenthesis"
                if number_of_unclosed_parenthesis < 0:
                    print("Cannot read infix expression. There seems to be an unclosed parenthesis.")
                    return self.ask_for_infix()
            elif character in App.operands:
                if previous_character == "operand":
                    print(f"Cannot read infix expression. There is a problem with '{infix[index -1]}' and '{character}'. Infix expressions must have an operator between operands.")
                    return self.ask_for_infix()
                previous_character = "operand"
                has_operand = True
            elif character in App.operators:
                if not has_operand:
                    print(f"Cannot read infix expression. There is a problem with '{character}'. Infix expressions must start with an operand.")
                    return self.ask_for_infix()

                elif previous_character == "operator":
                    print(f"Cannot read infix expression. There is a problem with '{infix[index -1]}' and '{character}'. Infix expressions must have an operand between operators.")
                    return self.ask_for_infix()
                has_operator = True
                previous_character = "operator"
            else:
                print(f"'{character}' is invalid.")
                return self.ask_for_infix()

        if number_of_unclosed_parenthesis != 0:
            print("Cannot read infix expression. There seems to be an unclosed parenthesis.")
            return self.ask_for_infix()

        if not has_operand or not has_operator:
            print("Infix expression must have an operator and an operand.") 
            return self.ask_for_infix()

        if infix[-1] in App.operators:
            print(f"Cannot read infix expression. There is a problem with '{infix[-1]}'. Infix expressions must end with an operand.")
            return self.ask_for_infix()

        return infix


    def try_again(self):
        ans = input("\nWould you like to try again? [y/n]:  ")
        try:
            match ans[0].lower():
                case "n":
                    sys.exit("\nThe program is closing ...\n")
                case "y":
                    self.main_menu()
                case _:
                    self.try_again()
        except IndexError:
            self.try_again()



if __name__ == "__main__":
    App()



# TODO
# COMMENTS, TESTING
