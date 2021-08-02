
class Dog:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color

    def get_name(self):
        return 'Dog ' + self.name

    def get_color(self):
        return self.color

    def shout(self):
      	return 'Dog ' + self.name + ': woof~'

