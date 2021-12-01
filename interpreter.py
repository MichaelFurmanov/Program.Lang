from nodes import *
from values import Number

class Interpreter:

    def __init__(self):
        pass

    def see(self, node):
        method = f'see_{type(node).__name__}'
        meth = getattr(self, method)
        return meth(node)

    def see_AddNode(self, node):
        return Number(self.see(node.node_a).value + self.see(node.node_b).value)

    def see_SubtractNode(self, node):
        return Number(self.see(node.node_a).value - self.see(node.node_b).value)

    def see_MultiplyNode(self, node):
        return Number(self.see(node.node_a).value * self.see(node.node_b).value)

    def see_IntegerNode(self, node):
        return Number(node.value)

    def see_StringNode(self, node):
        return Number(node.value)

    def see_PrintNode(self, node):
        return Number(self.see(node.node_a).value)

    def see_DivideNode(self, node):
        try:
            return Number(self.see(node.node_a).value / self.see(node.node_b).value)
        except:
            raise Exception("Ошибка вычислений")
