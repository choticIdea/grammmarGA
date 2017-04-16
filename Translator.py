
expr = "s";
operator = "opr";
var = "var";
plus = "+";
minus = "-";
times = "x";
division =":";
prev = "prev";
open = "open";
high = "high";
low = "low";
close = "close";



exprRules = [[var],[operator,expr,expr],[operator,expr,operator,expr]];
operatorRules = [plus,minus,times,division];
varRules = [prev,open,high,low,close];
literals = [plus,minus,times,division,prev,open,high,low,close];
stack = [expr];
formula = []

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

def bintodec(kromosom):
    dec = [];
    idx = 0;
    num = 0;
    for c in kromosom:
            if(idx > 0 and idx % 5 == 0):
                dec.append(num);
                num = 0;
            num+= 2^(idx % 5) * c;
            idx += 1;

    return dec
def translate(kromosom):
 for c in kromosom:

    print(stack)
    top = stack[len(stack)-1];
    if(isLiteral(top)):
        formula.append(stack.pop());
    if(len(stack) == 0):
        break;
    top = stack[len(stack) - 1];
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