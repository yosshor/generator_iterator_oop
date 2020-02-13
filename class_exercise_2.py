# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:45:02 2019

@author: EGLOBAL
"""

import numpy as np

class Pixel:
    def __init__(self, x = 0, y = 0, red = 0, green = 0, blue = 0):
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue
        
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    def set_grayscale(self):
        gray = np.mean([self.red, self.green, self.blue])
        self.red = gray
        self.blue = gray
        self.green = gray
        return
    
    def print_pixel_info(self):
        s = 'X:{}, Y:{}, Color:{}'.format(self.x, self.y, (int(self.red), int(self.green), int(self.blue)))
        if ((self.red and self.green) == 0) or ((self.blue and self.green) == 0) or ((self.red and self.blue) == 0):
            if self.red > 50:
                return s +' RED'
            if self.green > 50:
                return s + ' GREEN'
            if self.blue > 50:
                return s + ' BLUE'
        return s
    
    
my_pixel = Pixel(5, 6, 250, 0, 0)
print(my_pixel.print_pixel_info())
my_pixel.set_grayscale()
print(my_pixel.print_pixel_info())
    
    
    

#exercise 2.4  

class Bigthing:
    def __init__(self, variable):
        self.variable = variable
        
    def size(self):
        if isinstance(self.variable, int):
            return self.variable
        if isinstance(self.variable, (dict, list, str)):
            return ('the length of my name is : {}'.format(len(self.variable)))
  
    def __str__(self):
        return "my name is {}".format(self.variable) 
    

my_thing = Bigthing('balloon')
print(my_thing.size())     
print(my_thing)




class BigCat(Bigthing):
    def __init__(self, variable, weight):
        Bigthing.__init__(self, variable)
#        super().__init__(self, variable)
        self.weight = weight
        
    def size(self):
        print(super().size())
        if self.weight > 15 and self.weight < 20 :
            return 'And im Fat'
        elif self.weight > 20 :
            return 'And im Very Fat'
        return 'And im OK'

    def __str__(self):
        super().__str__()
        return "{} and my weight is {} kg".format(super().__str__(), self.weight)

cutie = BigCat('mutzy', 123)
print(cutie)
print(cutie.size())
 
    
    
    
    