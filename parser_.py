from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None

        result = self.exp()

        if self.current_token != None:
            self.error1()

        return result

    def exp(self):
        result = self.tok()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.tok())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.tok())

        return result

    def error1(self):
        raise Exception("Ошибка синтаксиса! ")

    def tok(self):
        result = self.ft()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.ft())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.ft())

        return result

    def ft(self):
        token = self.current_token

        if token.type == TokenType.PAREN_LEFT:
            self.advance()
            result = self.exp()

            if self.current_token.type != TokenType.PAREN_RIGHT:
                self.error1()

            self.advance()
            return result

        elif token.type == TokenType.INTEGER:
            self.advance()
            return IntegerNode(token.value)

        elif token.type == TokenType.STRING:
            self.advance()
            return StringNode(token.value)

        elif token.type == TokenType.PRINT:
            self.advance()
            return PrintNode(self.ft())

        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.ft())

        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.ft())

        self.error1()
