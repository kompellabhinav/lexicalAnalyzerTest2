import re
from typing import Union
from Stack import stack

def booleanEquation(equation):
    
    operators = [TList["Lesser"], TList["Greater"], TList["GreatEqual"], TList["LessEqual"], TList["Equal"], TList["NotEqual"]]

    for i in range(0, len(operators)):
        
        hasToken = f' {operators[i]} ' in equation

        if not hasToken:
            continue

        expression1, expression2 = equation.split(operators[i])

        value1 = expression(expression1)
        value2 = expression(expression2)

        tk = operators[i]

        if tk == operators[0]:
            return value1 < value2
        
        if tk == operators[1]:
            return value1 > value2
        
        if tk == operators[2]:
            return value1 >= value2
        
        if tk == operators[3]:
            return value1 <= value2
        
        if tk == operators[4]:
            return value1 == value2
        
        if tk == operators[5]:
            return value1 != value2

    raise Exception("Invalid boolean expression")

datatypes = {"Small", "Medium", "Large", "Huge"}

class BinaryNode:

    val: Union[str,int]

    def __init__(self, val = "") -> None:
        self.right = None
        self.left = None
        self.val = val


def indexPairBracket(st, startBracket, endBracket, startIndex):
    bracketCounter = 1
    currentIndex = startIndex + 1
    while bracketCounter > 0:
        if currentIndex >= len(st):
            raise Exception("Invalid Expression")
        if st[currentIndex] == startBracket:
            bracketCounter = bracketCounter + 1
        elif st[currentIndex] == endBracket:
            bracketCounter = bracketCounter - 1
        
        currentIndex = currentIndex + 1
    return currentIndex

def inParenthesis(exp):
    if exp[0] != TList["OPEN"]:
        return False
    val = indexPairBracket(exp, TList["OPEN"], TList["CLOSE"], 0)
    return val >= len(exp)

def tree(exp, node: BinaryNode):
    
    exp = exp.strip()

    if inParenthesis(exp):
        exp = exp[1:len(exp)-1]

    if not exp:
        raise Exception("Invalid Expression")

    if len(exp) == 0:
        return 

    if exp.isnumeric():
        node.val = int(exp)
        return

    temp = exp

    index_plus = None;
    index_minus = None;
    index_mul = None;
    index_div = None;

    i = 0 
    while i < len(temp):
        if temp[i] == TList["OPEN"]:
            i = indexPairBracket(temp, TList["OPEN"], TList["CLOSE"],i)
        elif temp[i-1:i+2] == f' {TList["DIVIDE"]} ':
            index_div = i
        elif temp[i-1:i+2] == f' {TList["PLUS"]} ':
            index_plus = i
        elif temp[i-1:i+2] == f' {TList["MINUS"]} ':
            index_minus = i
        elif temp[i-1:i+2] == f' {TList["MULTIPLY"]} ':
            index_mul = i
        
        i = i + 1

    
    if index_plus or index_minus or index_mul or index_div:
        node.left = BinaryNode("")
        node.right = BinaryNode("")
    else:
        if  exp not in stack or stack[exp][1] == None:
            raise Exception("Vairable does not exist")
        
        if stack[exp] != None:
            node.val = stack[exp][1]
        return 

    if index_mul:
        node.val = TList["MULTIPLY"]
        tree(exp[0:index_mul], node.left)
        tree(exp[index_mul+2:], node.right)
        return 

    if index_plus:
        node.val = TList["PLUS"]
        tree(exp[0:index_plus], node.left)
        tree(exp[index_plus+2:], node.right)
        return 
    
    if index_minus:
        node.val = TList["MINUS"]
        tree(exp[0:index_minus], node.left)
        tree(exp[index_minus+2:], node.right)
        return 
    
    if index_div:
        node.val = TList["DIVIDE"]
        tree(exp[0:index_div], node.left)
        tree(exp[index_div+2:], node.right)
        return 
    
    


def solveTree(node: BinaryNode):
    if not node:
        return 0
    
    if type(node.val) is int:
        return node.val
    
    if node.val == TList["PLUS"]:
        return solveTree(node.left) + solveTree(node.right)
    elif node.val == TList["MINUS"]:
        return solveTree(node.left) - solveTree(node.right)
    elif node.val == TList["MULTIPLY"]:
        return solveTree(node.left) * solveTree(node.right)
    elif node.val == TList["DIVIDE"]:
        denom = solveTree(node.right)
        if denom == 0:
            raise Exception("Division by Zero")
        return int(solveTree(node.left) / solveTree(node.right))


def expression(exp:str):
    exp = exp.strip()
    
    root = BinaryNode()

    tree(exp, root)
    return solveTree(root)

def insideBrackets(statement, startBracket, endBracket):
    
    bracketCounter = 1
    currentIndex = 1

    while bracketCounter > 0 :
        if statement[currentIndex] == startBracket:
            bracketCounter += 1
        elif statement[currentIndex] == endBracket:
            bracketCounter -= 1

        currentIndex += 1
    
    return [statement[1:currentIndex-1], statement[currentIndex:]]

TList = {
    'ASSIGNMENT': "=",
    'STOP': "stop",
    'PLAY': "play",
    'CONDITION': "condition",
    'LOOP': "loop",
    'PLUS': "+",
    'MINUS': "-",
    'MULTIPLY': "*",
    'DIVIDE': "/",
    'MODULUS': "%",
    'FLRDIV': "$",
    'Greater': ">",
    'Lesser': "<",
    'GreatEqual': ">=",
    'LessEqual': "<=",
    'Equal': "==",
    'NotEqual': "!=",
    'OPEN': "(",
    'CLOSE': ")",
    'BLOCKBEGIN': "{",
    'BLOCKFINISH': "}",
}
