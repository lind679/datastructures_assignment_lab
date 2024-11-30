class InfixToPostfixConverter:
    # Class to convert infix expression to postfix using a stack.

    def __init__(self):
        self.stack = []  # Stack to hold operators
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Operator precedence
        self.associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}  # Associativity of operators

    def is_operator(self, char):
        # Check if a character is an operator
        return char in self.precedence

    def is_operand(self, char):
        # Check if a character is an operand (alphanumeric).
        return char.isalnum()

    def precedence_of(self, operator):
        # Get the precedence of an operator.
        return self.precedence.get(operator, 0)

    def convert(self, infix):
        # Convert an infix expression to a postfix expression.
        postfix = []  # Output list for postfix expression

        for char in infix:
            if self.is_operand(char):
                postfix.append(char)  # Append operands directly to postfix
            elif char == '(':
                self.stack.append(char)  # Push '(' onto the stack
            elif char == ')':
                # Pop until '(' is encountered
                while self.stack and self.stack[-1] != '(':
                    postfix.append(self.stack.pop())
                self.stack.pop()  # Pop the '(' from the stack
            elif self.is_operator(char):
                # Pop operators from the stack while they have higher or equal precedence (left associative)
                while (self.stack and self.stack[-1] != '(' and
                       (self.precedence_of(self.stack[-1]) > self.precedence_of(char) or
                        (self.precedence_of(self.stack[-1]) == self.precedence_of(char) and self.associativity[char] == 'L'))):
                    postfix.append(self.stack.pop())
                self.stack.append(char)  # Push the current operator onto the stack

        # Pop remaining operators from the stack
        while self.stack:
            postfix.append(self.stack.pop())

        return ''.join(postfix)

# Example usage
if __name__ == "__main__":
    converter = InfixToPostfixConverter()
    infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
    print(f"Infix Expression: {infix_expression}")
    postfix_expression = converter.convert(infix_expression)
    print(f"Postfix Expression: {postfix_expression}")
