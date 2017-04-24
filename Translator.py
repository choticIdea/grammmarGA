
expr = "s";
operator = "opr";
var = "var";
plus = "+";
minus = "-";
times = "x";
division =":";
first = "first";
second = "second";
third = "third";
fourth = "fourth";
fifth = "fifth";



exprRules = [[var],[operator,expr,expr],[operator,expr,operator,expr]];
operatorRules = [plus,minus,times,division];
varRules = [first, second, third, fourth, fifth];
literals = [plus, minus, times, division, first, second, third, fourth, fifth];
stack = [expr];

def isOperator(token):
    if(token == plus or
       token == minus or
       token == times or
       token == division):
        return  True;
    else:
        return False;
def isLiteral(token):
   for lit in literals:
       if(token == lit):
           return True;
   return False;
def expressionRule(prodRule):
    appending = exprRules[prodRule];
    for t in appending:
        stack.append(t);
def operatorRule(prodRule):
        stack.append(operatorRules[prodRule]);
def variableRule(prodRule):
  stack.append(varRules[prodRule]);

#need state machine to verify the translation;
def placebo():
    return [plus, fifth, fourth];
def verify(prodCode):
    broken = False;
    stack = [];
    if(len(prodCode) == 0):
        return False;
    while(len(prodCode) != 0 and broken == False):

        if (isOperator(prodCode[len(prodCode) - 1]) == False and isLiteral(prodCode[len(prodCode) - 1]) == True):
            stack.append(var);
            prodCode.pop();
        elif(isOperator(prodCode[len(prodCode) - 1]) == True):
           prodCode.pop();
           if(len(stack) <= 1):
                broken = True
           else :
               stack.pop();

    if(broken) :
         return False # it is broken;
    elif(len(prodCode) == 0 and broken == False):
         return True # it is usable;
def translate(kromosom):
 formula = []
 for c in kromosom:

    if (len(stack) == 0):
         break;
    top = stack[len(stack)-1];
    if(isLiteral(top)):
        formula.append(stack.pop());
    if(top == expr ):
        stack.pop()
        expressionRule(c % len(exprRules))
    elif(top == operator):
        stack.pop()
        operatorRule(c % len(operatorRules));
    elif(top == var):
        stack.pop()
        variableRule(c % len(varRules));
 return formula;