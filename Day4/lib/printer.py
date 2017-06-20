def header(title):
    print('\n')
    print('=' * 46)
    print('=     {text: <38} ='.format(text=title))
    repeat('=' * 46, 2)
    repeat('\n', 2)


def repeat(text, nr):
    for i in range(nr):
        print(text)


def error(msg):
    print('Error: {}'.format(msg))