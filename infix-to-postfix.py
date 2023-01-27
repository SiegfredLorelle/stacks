import string
import sys
import re

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

    def peek(self):
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
    """ Manages communication between user and program """
    # Operands and operators are class variable to let the entire class use them
    operands = string.ascii_letters + string.digits
    # Maps operator with its level in order of operations (higher means first)
    operators = {
        "^": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1
    }


    def __init__(self):
        """ Launch the main menu immediately as soon as the app is initialized """
        self.main_menu()

    def main_menu(self):
        """ Display the postfix expression of the given infix expression """
        print("\n**********   Infix to Postfix Conversion   **********")

        # Ask infix expression then converts it to postfix expression
        infix = self.ask_for_infix()
        postfix = self.convert_to_postfix(infix)

        # Display the postfix expression
        print(f"\nPostfix expression:  {postfix}")

        # Prompt user if they want to try again
        self.try_again()


    def ask_for_infix(self):
        """ Returns the given infix expression after validating it """
        infix = input("\nEnter the infix expression:  ")
        infix = self.validate_infix(infix)
        return infix


    def convert_to_postfix(self, infix):
        """ Converting infix expression to postfix expression by using stacks """
        # Create a stack for the operators and the postfix expression
        operator_stack = Stack()
        postfix_stack = Stack()

        # Loop through each character of the infix expression
        for character in infix:

            # If it is an operand, then push it in postfix stack
            if character in App.operands:
                postfix_stack.push(character)

            # If it is an open parenthesis, then push it to operator stack
            elif character == "(":
                operator_stack.push(character)

            # If it is a closing parenthesis, then transfer all characters in operator stack to postfix stack until open parenthesis is on top of operator stack
            # If open parenthesis is on top of operator stack, then pop it
            elif character == ")":
                while (not operator_stack.is_empty() and operator_stack.peek() != "("):
                    postfix_stack.push(operator_stack.pop())
                operator_stack.pop()

            # If it is an operator, then check the level in order of operation of the element on top of the operator stack,
            # If the element on top has a higher or same level than the current character, then pop it
            # Continue popping, until current character has a higher level than the element on top
            # If current character has a higher level than the element on top, then push it operator stack
            else:
                # Continue popping until the current character has a higher level in order of operation than the top element of the operator stack
                while (not operator_stack.is_empty() and operator_stack.peek() != "(" and App.operators[operator_stack.peek()] >= App.operators[character]):
                        postfix_stack.push(operator_stack.pop())
                operator_stack.push(character)

        # After looping through the infix expression, transfer all all characters in operator stack to postfix stack
        else:
            while not operator_stack.is_empty():
                postfix_stack.push(operator_stack.pop())

        # Return the postfix stack (separate the characters with whitespace to make it readable)
        return " ".join(postfix_stack.stack)


    def validate_infix(self, infix):
        """ Ensures the given infix is valid """
        # Necessary variables to check its validity
        number_of_unclosed_parenthesis = 0
        previous_character = ""
        has_operand = has_operator = False

        # Change all square and curly brackets to regular brackets
        infix = re.sub("[\[{]", "(", infix)
        infix = re.sub("[]}]", ")", infix)
        # Remove all whitespaces
        infix = infix.replace(" ", "")

        # Loop through each character of the infix expression
        for index, character in enumerate(infix):

            # If it is an open bracket, then increment the number of unclosed parenthesis and set the previous character to be a parenthesis
            if character == "(":
                number_of_unclosed_parenthesis += 1
                previous_character = "parenthesis"

            # If it is a close bracket, then decrement the number of unclosed parenthesis and set the previous character to be a parenthesis 
            # If number of unclosed parenthesis is negative, then inform user about an error and ask for another infix expression
            elif character == ")":
                number_of_unclosed_parenthesis -= 1
                previous_character = "parenthesis"
                if number_of_unclosed_parenthesis < 0:
                    print("Cannot read infix expression. There seems to be an unclosed parenthesis.")
                    return self.ask_for_infix()

            # If it is an operand and the previous character is also an operand, then inform user about error and ask for another infix expression
            # If valid, then set the previous character to be operand and set has operand to true
            elif character in App.operands:
                if previous_character == "operand":
                    print(f"Cannot read infix expression. There is a problem with '{infix[index -1]}' and '{character}'. Infix expressions must have an operator between operands.")
                    return self.ask_for_infix()
                previous_character = "operand"
                has_operand = True

            # If it is an operator and there is still no operand, then inform the user about the error and ask for another infix expression
            # If the previous character is also an operator, then inform the user about the error and ask for another infix expression
            # If valid then set the previous character to be an operator and set has operator to true
            elif character in App.operators:
                if not has_operand:
                    print(f"Cannot read infix expression. There is a problem with '{character}'. Infix expressions must start with an operand.")
                    return self.ask_for_infix()
                elif previous_character == "operator":
                    print(f"Cannot read infix expression. There is a problem with '{infix[index -1]}' and '{character}'. Infix expressions must have an operand between operators.")
                    return self.ask_for_infix()
                has_operator = True
                previous_character = "operator"

            # If it is not a parenthesis, nor a operator nor a operand, then it is an invalid character
            else:
                print(f"'Cannot read infix expression. '{character}' is invalid.")
                return self.ask_for_infix()

        # If the number of unclosed parenthesis is not 0, then there is an open parenthesis
        if number_of_unclosed_parenthesis != 0:
            print("Cannot read infix expression. There seems to be an unclosed parenthesis.")
            return self.ask_for_infix()

        # If there is no operand or no operator, then it is invalid
        if not has_operand or not has_operator:
            print("Infix expression must have an operator and an operand.") 
            return self.ask_for_infix()

        # If the last character of the infix expression is an operator, then it is invalid
        if infix[-1] in App.operators:
            print(f"Cannot read infix expression. There is a problem with '{infix[-1]}'. Infix expressions must end with an operand.")
            return self.ask_for_infix()

        # If the infix expression pass all the validity test, then return the valid infix
        return infix


    def try_again(self):
        """ Prompts for a try again question """
        # Asks for the a response
        response = input("\nWould you like to try again? [y/n]:  ")
        # Catches error where user pressed enter without a response (Entered Null or None)
        try:
            # If yes then go back to main menu, if no then exist program, if invalid then ask this question again
            match response[0].lower():
                case "n":
                    sys.exit("\nThe program is closing ...\n")
                case "y":
                    self.main_menu()
                case _:
                    self.try_again()
        except IndexError:
            self.try_again()


# Launches the app
if __name__ == "__main__":
    App()