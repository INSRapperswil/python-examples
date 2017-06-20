print('Is false equal true?')
print(False == True)

print('Is 5 equal \'5\'?')
print(5 == '5')

print('Is 7 equal int(\'7\')?')
print(7 == int(7))

print('Is 11 equal 11.0?')
print(11 == 11.0)

print('Is \'duplex\' unequal \'halfduplex\'?')
print('duplex' != 'halfduplex')

print('Is \'duplex\' a part of \'halfduplex\'?')
print('duplex' in 'halfduplex')

color = 'blue'
if color == 'red':
    print('Your color is red')
else:
    print('Your color is not red')

counter = 10
while counter > 0:
    print(counter)
    counter = counter - 1

while True:
    my_color = input('Enter a color (blue, red, green): ')
    if my_color in ['blue', 'red', 'green']:
        print('Your color is {color}'.format(color=my_color))
        break

for index in range(10):
    print('Index (range): {}'.format(index))

for index in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print('Index (list): {}'.format(index))

answer = input('Are you sure? [yes/no]')
yes = ['y', 'yes', 'ja']
if answer.lower() in yes:
    print('You are sure!')
