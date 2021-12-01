from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
	PLUS = 1
	MINUS = 2
	MULTIPLY = 3
	DIVIDE = 4
	INTEGER = 5
	STRING = 6
	PRINT = 7
	PAREN_LEFT = 8
	PAREN_RIGHT = 9
	
@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")
