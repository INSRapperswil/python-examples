class Person:
    body = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def format_print(self):
        print('Name {}\tAlter: {}'.format(self.name, self.age))

    @staticmethod
    def get_body():
        return Person.body


hans = Person('hans', 30)
urs = Person('urs', 29)
participants = [hans, urs]

for person in participants:
    person.format_print()

print('{name} has {body} body'.format(name=urs.name, body=urs.get_body()))

print('class variable')
print(id(Person.body))
print(id(hans.body))
print(id(urs.body))
print(id(Person.get_body()))
print(id(urs.get_body()))
print(id(hans.get_body()))

print('object variable')
print(id(urs.age))
print(id(hans.age))
