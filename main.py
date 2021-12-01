from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
print("ЯЗЫК ПРОГРАММИРОВАНИЯ ERM. ФУРМАНОВ МИХАИЛ, ПОИТ-2")
while True:
    try:
        text = input("Введите выражение: ")
        print("Длинна текста: ", len(text))
        print("Извлечение подстроки: ", text[2])
        print("-----------------------------------")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print("Вывод: ", value)
        print()
    except Exception as error:
        print(error)
