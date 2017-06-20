def addition(augend, addend):
    total = augend + addend
    return total


def subtraction(minuend, subtrahend):
    difference = minuend - subtrahend
    return difference


def multiplication(multiplicand, multiplier):
    product = multiplicand * multiplier
    return product


def division(dividend, divisor):
    if divisor == 0:
        print('division by zero is undefined')
        return
    quotient = dividend / divisor
    return quotient


def print_header(title):
    print('\n')
    print('-' * 36)
    print('-     {text: <28} -'.format(text=title))
    print('-' * 36)


print_header('I love math')
a = int(input('a: '))
b = int(input('b: '))

print_header('a + b')
r = addition(a, b)
print(r)

print_header('b + a')
print(addition(b, a))

print_header('a - b')
print(subtraction(minuend=a, subtrahend=b))

print_header('b - a')
print(subtraction(b, a))

print_header('a / (a / b)')
c = division(a, b)
r = division(dividend=a, divisor=c)
print(r)

print_header('(a - b) * a * b')
print(multiplication(multiplication(subtraction(a, b), a), b))

print_header('(a * b) / (a - b - a + b)')
x = multiplication(a, b)
# y = (a - b ) + ( -a + b )
y = addition(augend=subtraction(minuend=a, subtrahend=b), addend=addition(augend=-a, addend=b))
print('{dividend} / {divisor}'.format(dividend=x, divisor=y))
print(division(dividend=x, divisor=y))
