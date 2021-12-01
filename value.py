from dataclasses import dataclass

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"

@dataclass
class IntegerNode:
    value: any

    def __repr__(self):
        return f"{self.value}"

@dataclass
class StringNode:
    value: any

    def __repr__(self):
        return f"{self.value}"

@dataclass
class PrintNode:
    node_a: any

    def __repr__(self):
        return f"({self.node_a})"

@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"
