from misc import *

def statement(self):
    self = self.strip()

    if not self:
        return
    
    regex_intialWord = re.findall("^[a-zA-Z]* ", self)

    if not regex_intialWord:
        raise Exception("Invalid Syntax")
    
    initalWord = regex_intialWord[0].strip()

    if initalWord in  datatypes :
        declaration(self)

    elif initalWord == TList['LOOP']:
        loop(self)

    elif initalWord == TList['CONDITION']:
        condition(self)

    elif initalWord in stack:
        assign(self)

    else:
        raise Exception(f'{initalWord} is not defined')


def assign(self):
   
    rmatch = re.findall("([^;]+);(.*)", self.strip())

    assignStatement = rmatch[0][0]
    restStatement = rmatch[0][1]

    variable, expr = assignStatement.split("=")

    variable = variable.strip()
    expr = expr.strip()

    stack[variable][1] = expression(expr)
    statement(restStatement.strip())

def condition(self):
    self = self.replace("condition ", "", 1)

    [booleanStatement, restStatement] = insideBrackets(self, TList["OPEN"], TList["CLOSE"])
    [insideStatement, restStatement] = insideBrackets(restStatement.strip(), TList["BLOCKBEGIN"], TList["BLOCKFINISH"])

    if booleanEquation(booleanStatement):
        statement(insideStatement)

    statement(restStatement)

def declaration(self):
    rmatch = re.split("([^;]+);(.*)", self.strip())
    
    stStatement = rmatch[1]
    restStatement = rmatch[2]
    
    vType, variable = stStatement.split(" ")

    vType = vType.strip()
    variable = variable.strip()

    if variable in stack:
        raise Exception("{} is already there".format(variable))

    stack[variable] = [vType, None]
    statement(restStatement.strip())

def loop(self):
    
    self = self.replace("loop ", "", 1).strip()
    [boolStatement, restStatement] = insideBrackets(self, TList["OPEN"], TList["CLOSE"])
    [ifStatement, restStatement] = insideBrackets(restStatement.strip(), TList["BLOCKBEGIN"], TList["BLOCKFINISH"])

    while True:
        if booleanEquation(boolStatement):
            statement(ifStatement)
        else:
            break
    
    statement(restStatement)