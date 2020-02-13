
"""
@author: Yossi
"""

class Animal:
    """This class used to represent an animal"""
    def __init__(self, name, hunger = 0, zoo_name = 'Hayaton'):
        self._name = name
        self._hunger = hunger
        self.zoo_name = zoo_name
        
    def get_name(self):
        return self._name
    
    def is_hungry(self):
        if self._hunger > 0:
            return True
        return False
    
    def feed(self):
        self._hunger =- 1
        
    def talk(self):
        return 'Each Animal have a diffrence talk'

    def __str__(self):
        return 'Our zoo name is {}'.format(self.zoo_name)


class Dog(Animal):
    """This class inheritor the structure from the Animal class, with more specific function to represent a Dog """
    def __init__(self, _name, _hunger):
        Animal.__init__(self, _name, _hunger)
        
    def talk(self):
        return 'Barks woof woof'

    def fetch_stick(self):
        return 'There you go,sir!'


class Cat(Animal):
    """This class inheritor the structure from the Animal class, with more specific function to represent a Cat """
    def __init__(self, _name, _hunger):
        Animal.__init__(self, _name, _hunger)
    
    def talk(self):
        return 'meow'
    
    def chase_laser(self):
        return 'Meeeeow'


class Skunk(Animal):
    """This class inheritor the structure from the Animal class, with more specific function to represent a Skunk """
    def __init__(self, _name, _hunger, _stink_count = 6):
        Animal.__init__(self, _name, _hunger)
        self._stink_count = _stink_count
    
    def talk(self):
        return 'tsssss'
    
    def stink(self):
        return 'Deer lord!'
        
    
class Unicorn(Animal):
    """This class inheritor the structure from the Animal class, with more specific function to represent a Unicorn"""
    def __init__(self, _name, _hunger):
        Animal.__init__(self, _name, _hunger)
     
    def talk(self):
        return 'Good day, darling'   
    
    def sing(self):
        return "I'm not your toy..."


class Dragon(Animal):
    """This class inheritor the structure from the Animal class, with more specific function to represent a Unicorn"""
    def __init__(self, _name, _hunger, _color = 'Green'):
        Animal.__init__(self, _name, _hunger)
        self._color = _color
        
    def talk(self):
        return 'Raaaawr'

    def breath_fire(self):
        return '$@#$#@$'        


def check_class(animal):
    """This function gets an Animal and checks to which class its connected.
    :param animal: animal value
    :type animal: class
    :return: The result is the special method for an correct animal 
    :rtype: str
    """
    if isinstance(animal, Dog):
       return animal.fetch_stick()
    if isinstance(animal, Cat):
        return animal.chase_laser()
    if isinstance(animal, Skunk):
        return animal.stink()
    if isinstance(animal, Unicorn):
        return animal.sing()
    if isinstance(animal, Dragon):
        return animal.breath_fire()


def main():
    """This function combinnig all other functions and classes together and call the right function or class for to do the 
      right things, at the beginig i initialize all the animals and combine them together in one list, and print for each animal 
      in the list her name and the special method and also the axactly voice/talk for animal. 
      and at the end we print the name of our zoo
    """    
    my_dog = Dog('Brownie', 10)
    my_cat = Cat('Zelda', 3)
    my_skunk = Skunk('Stinky', 0)
    my_unicorn = Unicorn('Keith', 7)
    my_dragon = Dragon('Lizzy', 1450) 
    another_dog = Dog('Doggo', 80)
    another_cat = Cat('Kitty', 80)
    another_skunk = Skunk('Stinky Jr.', 80)
    another_unicorn = Unicorn('Clair', 80)
    another_dragon = Dragon('McFly', 80)
    zoo_list = [my_dog, my_cat, my_skunk, my_unicorn, my_dragon, another_dog, another_cat,
                another_skunk, another_unicorn, another_dragon]
    for animal in zoo_list:
        if not animal.is_hungry():
            print(animal.talk())
            print(check_class(animal))
        while animal.is_hungry():
            animal.feed()
            print(type(animal).__name__, animal.get_name(), animal.talk())
            print(check_class(animal))
    print(animal)

if __name__ == "__main__":
    main()
