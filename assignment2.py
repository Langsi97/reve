class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)  # adds element to the stack.

    def pop(self):  # remove the last element added as the first
        if self.is_empty():  # check if the stack is empty, if yes then raise error
            raise KeyError("You can not pop an empty stack.")
        return self._items.pop()

    def is_empty(self):  # remove all element from  the stack
        return len(self._items) == 0


# question 2 of assigntment 2


class InfixExpression:
    def __init__(self, expression):  # initializing the expression argurment.
        self._expression = expression

    @property  # property decorator for the object expression.
    def expression(self):
        return self._expression

    @expression.setter  # attributing the argument expression to self._expression.
    def expression(self, expression):
        self._expression = expression

    # function to update the the given expression to a new expression.

    def update_expression(self, operator, expression_2):
        self._expression = f"({self._expression}){operator}({expression_2})"

    # creating an object to convert infix to postfix.

    def convert_to_postfix(self):
        pass
