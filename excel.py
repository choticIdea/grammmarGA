from  xlrd import *
a = [[1,2,3],[3,2,1]];
plus = "+";
close = 0;
open =  1;
low = 2;
order = [plus,open,low];
print(a[1][2])
stack = [];
res = 0;
while len(order) != 0 :
    if(order[len(order)-1] != plus):
        stack.append(a[0][order.pop()]);
    else :
       res = stack.pop()+stack.pop();
       stack.append(res)
       order.pop();

print(stack.pop())

