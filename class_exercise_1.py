

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:47:33 2019

@author: EGLOBAL
"""


from itertools import count

#**kwargs
class Animals:
    x = count(1)
    def __init__(self, age, name = 'Octavio'):
        self.name = name
        self.age = age
        self.b = 0
        self.id_c = next(self.x)
        
    def birthday(self):
        return self.age + 1

    def get_age(self):
        return self.age
    
    def get_count(self):
        self.b+=1
        return self.b
#        d += 1 #self.b + 1
#        return d
    
    def set_name(self, name):
        self.name = name
        return self.name 
    
    def get_name_and_age(self):
        return self.name, self.age
    
    def get_name(self):
        return self.name
 


def main():
#    a = Animals('octopus', 12)
    a = Animals(13)
    print(a.name, a.age)
#    print(a.get_name_and_age())
    a.set_name('Octipus')
    a.age = 12
    print(a.name, a.age)
    print(' bring me the name ', a.get_name())
    print(a.get_name_and_age())
    print('and her age is :', a.birthday())
    b = Animals(name = 'lion', age = 12)
    print(b.get_name_and_age())
    print('her age is :',b.get_age())
    e=Animals('e',3)
#    print(e.get_count())
    print(e.id_c)
    c = Animals('l',5)
#    print(c.get_count())
    print(c.id_c)
    print('here we define {} classes'.format(c.id_c))

main()



#
#class Question:
#    def __init__(self):
#        self.a = 0
#    def func(self):
#        print(self)
#def main():
#    A = Question()
#    A.func()
#main()
#
