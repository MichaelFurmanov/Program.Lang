from tokens import Token, TokenType
STR = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
DIGITS = '0123456789-1-2-3-4-5-6-7-8-9'

STR_DIGITS = DIGITS + STR
WHITESPACE = ' \n\t'

PR = '$'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_integer()

            elif self.current_char in STR:
                yield self.generate_str()

            elif self.current_char == '$':
                yield self.generate_print()

            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.PAREN_LEFT)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.PAREN_RIGHT)
            else:
                raise Exception(f"Запрещенный символ! '{self.current_char}'")

    def generate_integer(self):
        count = 0
        int_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                count += 1
                if count > 1:
                    break

            int_str += self.current_char
            self.advance()

        return Token(TokenType.INTEGER, int(int_str))

    def generate_str(self):
        num_str = self.current_char
        self.advance()
        while self.current_char != None and (self.current_char == ',' or self.current_char in STR_DIGITS):
            num_str += self.current_char
            self.advance()

        return Token(TokenType.STRING, str(num_str))


    def generate_print(self):
        num_str = self.current_char
        self.advance()
        while self.current_char != None and (self.current_char in PR):
            num_str += self.current_char
            self.advance()

        return Token(TokenType.PRINT)
