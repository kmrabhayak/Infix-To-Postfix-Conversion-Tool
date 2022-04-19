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

Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators


def infixToPostfix(expression):
    stack = []  # initialization of empty stack

    output = ''

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output += character

        elif character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output += stack.pop()

    return output

from colorama import Back,Fore,Style
expression = input(Back.LIGHTWHITE_EX+ Fore.RED+'\n\nEnter Infix Expression ')

print(Back.LIGHTWHITE_EX+ Fore.RED+'\nInfix Notation: ', expression)
result=infixToPostfix(expression)


print(Back.LIGHTWHITE_EX+ Fore.RED+'\nPostfix Notation: ', result)

print(Style.RESET_ALL)
input(Back.LIGHTWHITE_EX+ Fore.RED+"Enter any key to Quit")
