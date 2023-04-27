
import re


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)  # adds element to the stack.

    def pop(self):  # remove the last element added as the first
        if self.is_empty():
            # check if the stack is empty, if yes then raise error
            raise KeyError("You can not pop an empty stack.")
        return self._items.pop()

    def is_empty(self):  # remove all element from  the stack
        return len(self._items) == 0


"""--------------------------------"""
# question 2 of assigntment 2


class InfixExpression:
    def __init__(self, expression):  # initializing the expression argurment.
        self._expression = expression

    @property  # property decorator for the object expression.
    def expression(self):
        return self._expression

    # attributing the argument expression to self._expression.
    @expression.setter
    def expression(self, expression):
        self._expression = expression

    # function to update the the given expression to a new expression.

    def update_expression(self, operator, expression_2):
        self._expression = f"({self._expression}){operator}({expression_2})"

    # creating an object to convert infix to postfix.

    def convert_to_postfix(self):
        # dictionary to store operation signs in order of preference.
        operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []    # empty stack  to store the operators
        postfix_output = ''     # empty string to store the output

        # using regex to match all characters in the infix expression

        for character in re.findall(r'[\w]+|\S', self._expression):
            # if the character is alphanumeric add
            #  it to the postfix_output variable
            if character.isalnum():
                postfix_output += character
            # if the character is an open bracket add it to the stack.
            elif character == '(':
                stack.append(character)
            # check if the character is a closing bracket and pop out the
            # operators in order of precedence to the postfix_output until we
            # encouter an open paranthesis
            elif character == ')':
                while stack[-1] != '(':
                    # If element is a right parenthesis, pop from stack until
                    # a matching left parenthesis is found
                    postfix_output += stack.pop()
                stack.pop()
            else:
                # If element is an operator, pop operators with higher
                # precedence from stack and append to output
                while (stack and stack[-1] != '(' and
                       operators.get(stack[-1], 0)
                       >= operators.get(character, 0)):
                    postfix_output += stack.pop()
                stack.append(character)
        # pop any remaining operators from stack and add them to postfix_
        # output string
        while stack:
            postfix_output += stack.pop()
        return postfix_output
