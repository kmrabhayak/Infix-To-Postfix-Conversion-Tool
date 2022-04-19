# Python program to convert infix expression to postfix expression
#!/usr/bin/env python
from time import sleep

def progress(percent=0, width=30):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)
from colorama import Back,Fore
print(Fore.RED+ Back.LIGHTWHITE_EX+'Credits @kmr_abhay\nLoading ')
for i in range(101):
    progress(i)
    sleep(0.1)

# Newline so command prompt isn't on the same line
print()

top = -1


def push(value):
    global top
    top += 1
    stack.append(value)


def pop():
    global top
    if (top == -1):
        print("Exit")
    else:
        x = stack.pop()
        top -= 1
        return x


'''
def evaluation(target_list):
    for i in target_list:
    if(i>='0' and i<='9'):
        push(i)
    else:
        x = pop()
        y = pop()
        result = operation(x,y,i)
        push(result)
postfix = stack[top]
print(postfix)
'''


def operation(a, b, op):
    a = int(a)
    b = int(b)
    if (op == '+'):
        return a + b
    elif (op == '-'):
        return a - b
    elif (op == '*'):
        return a * b
    elif (op == '/'):
        return a / b
    elif (op == '^'):
        return pow(a, b)

from colorama import Fore, Back, Style
print(Back.LIGHTWHITE_EX + Style.BRIGHT+ Fore.RED+'                Infix To Postfix')
print(Style.BRIGHT + '')
expression = input(Fore.RED+ Back.LIGHTWHITE_EX+"              Enter the expression \n")
expression_list = []
operand = ""
stack = []

priority_op = {'-': 1, '+': 2, '/': 3, '*': 4, '^': 5}

for i in expression:
    if ((i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9')):
        operand += i
    else:
        if (operand != ""):
            expression_list.append(operand)
            operand = ""
        expression_list.append(i)
if (operand != ""):
    expression_list.append(operand)
print(expression_list)

target_list = []

for i in expression_list:
    if ((i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9')):
        target_list.append(i)
    else:
        if (top == -1):
            push(i)
        elif (i == '('):
            push(i)
        elif (i == ")"):
            while (stack[top] != '('):
                x = pop()
                target_list.append(x)
            if (stack[top] == '('):
                pop()
        elif (stack[top] == '('):
            push(i)
        elif (priority_op[i] > priority_op[stack[top]]):
            push(i)
        elif (priority_op[i] < priority_op[stack[top]]):
            x = pop()
            target_list.append(x)
            push(i)
while (top >= 0):
    x = pop()
    target_list.append(x)

print(target_list)

for i in target_list:
    if (i >= '0' and i <= '9'):
        push(i)
    else:
        x = pop()
        y = pop()
        result = operation(x, y, i)
        push(result)

postfix = stack[top]
print(postfix)
print(Style.RESET_ALL)
