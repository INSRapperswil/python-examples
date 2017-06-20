class Player:
    def __init__(self, length):
        self.x = 0
        self.y = 0
        self.step_length = length

    def right(self):
        self.x += self.step_length

    def left(self):
        self.x -= self.step_length

    def up(self):
        self.y += self.step_length

    def down(self):
        self.y -= self.step_length

    def position(self):
        return self.x, self.y

    def name(self):
        return('I\'m a player')


class Frog(Player):
    def __init__(self):
        Player.__init__(self, 3)

    def name(self):
        return('I\'m a frog')


class Bug(Player):
    def __init__(self):
        Player.__init__(self, 1)

    def name(self):
        return('I\'m a bug')


bug = Bug()
bug.down()
bug.right()
print(bug.position())   # (1, -1)
print(bug.name())       # I'm a bug

frog = Frog()
frog.left()
frog.up()
print(frog.position())  # (-3, 3)
print(frog.name())      # I'm a frog
