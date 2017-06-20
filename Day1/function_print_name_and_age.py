def pretty_text(name, age):
    text = 'My name is {0} and I\'m {1} years old.'
    return text.format(name, age)

my_name = input('Name: ')
my_age = input('Age: ')

text_to_print = pretty_text(my_name, my_age)
print(text_to_print)
