from exp_root.root import *
from exp_root.exponention import *
from factorial.factorial import fact
from logarithm.logarithm import *


def check(a, typee):
    try:
        typee(a)
        return True
    except:
        return False


if __name__ == '__main__':
    print('Menu:\nPlease choose one function:')
    print('1) factorial')
    print('2) logarithm')
    print('3) exponent or root')
    while True:
        n = input('Choose 1, 2 or 3')
        if n == '1' or n == '2' or n == '3':
            break
        print('Error in the input')
    print('_' * 8)
    if n == '1':
        print('You have chosen factorial function')
        while True:
            n = input('Enter the natural number:')
            if n.isdigit() and n != '0':
                break
            print('Error in the input')
        print('Factorial of {} is {}'.format(n, fact(int(n))))
    elif n == '2':
        print('You have chose logarithm function')
        print('Please choose one function: ')
        print('1) log')
        print('2) ln')
        print('3) lg')
        while True:
            n = input('Choose 1, 2 or 3')
            if n == '1' or n == '2' or n == '3':
                break
            print('Error in the input')
        print('_' * 8)
        if n == '1':
            print('You have chosen the log:')
            while True:
                a = input('Please enter the base of the logarithm')
                if check(a, float) and a[0] != '-' and a != '0' and a != '1':
                    break
                print('Error in the input')
            while True:
                b = input('Please enter number')
                if check(b, float) and b[0] != '-' and b != '0':
                    break
                print('Error in the input')
            n = [float(a), float(b)]
            func = log
        elif n == '2':
            print('You have chosen the ln:')
            while True:
                b = input('Please enter number')
                if check(b, float) and b[0] != '-' and b != '0':
                    break
                print('Error in the input')
            n = [float(b)]
            func = ln
        elif n == '3':
            print('You have chosen the lg:')
            while True:
                b = input('Please enter number')
                if check(b, float) and b[0] != '-' and b != '0':
                    break
                print('Error in the input')
            n = [float(b)]
            func = lg
        print('Logarithm of {num} = {func}'.format(num=str(n), func=func(*n)))
    elif n == '3':
        print('You have chosen exp_root function')
        print('Please choose one function: ')
        print('1) exp in 2')
        print('2) exp in 3')
        print('3) root in 2')
        print('4) root in 3')
        while True:
            n = input('Choose 1, 2, 3 or 4')
            if n == '1' or n == '2' or n == '3' or n == '4':
                break
            print('Error in the input')
        print('_' * 8)
        if n == '1':
            print('You have chosen exp in 2')
            while True:
                a = input('Please enter number')
                if check(a, float):
                    break
                print('Error in the input')
            func = exp2
        elif n == '2':
            print('You have chosen exp in 3')
            while True:
                a = input('Please enter number')
                if check(a, float):
                    break
                print('Error in the input')
            func = exp3
        elif n == '3':
            print('You have chosen root in 2')
            while True:
                a = input('Please enter number')
                if check(a, float) and float(a) >= 0:
                    break
                print('Error in the input')
            func = root2
        elif n == '4':
            print('You have chosen root in 3')
            while True:
                a = input('Please enter number')
                if check(a, float) and float(a) >= 0:
                    break
                print('Error in the input')
            func = root3
        print('Result of the operation is {}'.format(round(func(float(a))),3))
