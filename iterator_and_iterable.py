# -*- coding: utf-8 -*-
"""
@author: Yoss
"""

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

split_notes = [(i) for i in notes.split('-')]
print(dir(split_notes))
print(type(split_notes))
for i in split_notes:
    print(i)
    
    
    
import winsound
# Play the song yonatan hakatan
def play():
    fre = []
    duration = []
    c = []
    for i in split_notes:
        fre.append(i.split(',')[0])
        duration.append(i.split(',')[1])
        c.append(i.split(','))
    for i in range(len(fre)):
        winsound.Beep(int(freqs[fre[i]]), int(duration[i]))
    
play()        
        
# how to show the third num in numbers without using if condition
numbers = iter(list(range(1, 101, 3)))       
print(next(numbers))

print(numbers)

numbers = iter(list(range(1, 101)))       
for i in numbers:
    next(numbers)
    next(numbers)
    print(i)
    


import itertools
import numpy as np
my_bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
#all_combinations = itertools.permutations(my_bills)

all_combinations = (itertools.combinations(my_bills, i) for i in range(0, 15))
sum_of_possible_option = []
for i in all_combinations:
    for j in i:
        if np.sum(j) == 100:
            sum_of_possible_option.append(j)

sum_of_possible_option = set(sum_of_possible_option)
print(sum_of_possible_option)
print(len(sum_of_possible_option))



sum_com = [i for i in all_combinations if np.sum(i) > 10]
print(len(sum_com))
print(next(all_combinations))
print(next(np.sum(all_combinations, axis = 0)))



class Employee:
    
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary
        
    def get_name(self):
        return self._name



class EmployeeManager:
    
    def __init__(self):
        self._employee_lst = []
        self.empl_index = -1
        
    def add_employee(self, new_empl):
        self._employee_lst.append(new_empl)
    
    def return_employeeds(self):
        return self._employee_lst

    def __iter__(self):
        return self

    def __next__(self):
        if self.empl_index >= len(self._employee_lst) -1:
            raise StopIteration()
        self.empl_index += 1
        return self._employee_lst[self.empl_index].get_name()

manager = EmployeeManager()
manager.add_employee(Employee("Lia Levi", 30, 5000))
manager.add_employee(Employee("Yosef Cohen", 32, 4800))
manager.add_employee(Employee("Oded Haim", 47, 5100))

for i in manager:
    print(i)

print(manager.__next__())




import numpy as np

class MusicNotes:
    
    def __init_(self):
        self.table = []
        self.index = -1
        

    def multiplay(self):
        self.freqs = {"la": 55,
                     "si": 61.74,
                     "do": 65.41,
                     "re": 73.42,
                     "mi": 82.41,
                     "fa": 87.43,
                     "sol": 98,
             }
        self.just_fre = [self.freqs[i]  for i in self.freqs.keys()]
        self.count = 0
        self.t = np.array(self.just_fre)
        self.table = []
        self.table.append(self.just_fre)
        while self.count < 4:
            self.t *= 2
            self.table.append(list(self.t))
            self.count += 1
        return self.table
    
    def get_freq(self):
        return self.table

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.table[self.index == 1568]:
            raise StopIteration()
        self.index += 1
        return self.table[self.index]
    
print(next(f))


f = MusicNotes()
print(f.multiplay())
[j for i in f.multiplay() for j in i]
print(f.get_freq())
print(next(f))

g = [freqs[i]  for i in freqs.keys()]

count = 0
t = np.array(g) 
table = []
table.append(g)

while count < 4:
    t *= 2
    table.append(list(t))
    print(t)
    count += 1

d = [i * 2 for i in g]
















 
    