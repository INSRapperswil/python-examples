def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def chatty_fib(n):
    if n <= 1:
        print('Return {}'.format(n))
        return n
    else:
        print('Return: chatty_fib({0}-1) + chatty_fib({0}-2)'.format(n))
        return chatty_fib(n-1) + chatty_fib(n-2)


print('Calculate fibonacci')
input_n = input('n: ')
n = int(input_n)
f = fib(n)
print(f)

input('The show must go on!')
print('=' * 30)
print(chatty_fib(n))
