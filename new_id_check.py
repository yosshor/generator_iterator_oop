"""
@author: Yoosi
"""

import numpy as np

class globalException(Exception):
    """ That class inherit from global Exception class, and build the structure for another classes who want to inherit 
        that structure for another exception class.
    """    
    def __init__(self, id_number):
        self.id_number = id_number
    
    def __str__(self):
        return "its depand on your exception"
    
    def get_id_number(self):
        return self.id_number


class Idtooshort(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_nimber is too short, that means the user inserted less digits for id numbers.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
    
    def __str__(self):
        return "Your id number is too short, it must be equal to 9 numbers"
    
    
class Idtoolong(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_nimber is too long, that means the user inserted more digits for id numbers.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is too long, the id number must be equal to 9 numbers"
 
    
class ID_num_missing_digit(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_number is not valid, that means the user inserted letters for id numbers, and the user only 
        could insert digits.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is not valid, you need to insert only numbers" 
    

def check_zeros(id_num):
    """ That function checks if the id_number is contains 9 real digits without zeros at the begining,
        if id_num has zeros at the begining the function remove them.
        :param id_num: id_num value
        :type id_num: str
        :raise: Idtooshort if id_num is less then 9 digits
        :return: True if the id_num dont have zeros at the beginig, else raise an exception that tell 
        the user that he need to insert only 9 digits without zeros at the begining.
       :rtype: bool 
    """  
    try:
        id_num = int(id_num)
        if len(str(id_num)) < 9:
            raise Idtooshort(id_num)
    except Idtooshort:
        print(Idtooshort.__str__(id_num) + str(" without zeros at the begining"))
    else:
        return True
        

    
id_num  = '309892334'
int(id_num)
check_zeros(id_num)

def check_id_number(id_number): 
    """ That function checks if the id_number is correct, it checks if the id number have zeros
        at the beginig of the number, if yes the function remove them.
        :param id_num: id_num value
        :type id_num: str
        :raise: Idtooshort if id_num is less then 9 digits
        :return: True if the id_num dont have zeros at the beginig, else raise an exception that tell 
        the user that he need to insert only 9 digits without zeros at the begining.
       :rtype: bool 
    """ 
    first = [int(j) * 2  if (i + 1) % 2 == 0 else int(j) for i, j in enumerate(str(id_number))  ]
    first = [str(i) for i in first]
    second = [(int(num[0]) + int(num[1]))  if int(num) > 9 else num for i, num in enumerate(first)]
    the_sum = np.sum(np.array(second, dtype = int))  # I can do it with loop and one variable that sum all i in loop to the variable
    if the_sum % 10 == 0:
        return True
    return False


def check_id_valid(id_number):
    """ That function checks if the id_number is correct, it checks if the id number have zeros
        at the beginig of the number, if yes the function remove them.
        :param id_number: id_number value
        :type id_number: str
        :raise: Idtooshort if id_number is less then 9 digits.
        :raise: Idtoolong if id_number is more then 9 digits.
        :raise: ID_num_missing_digit if id_number not contains oonly digits.
        :return: True if the id_number contains 9 real correct digits, else False.
        :rtype: bool 
    """
    try :
        if len(id_number) < 9:
            raise Idtooshort(id_number)
        if len(id_number) > 9:
            raise Idtoolong(id_number)
        if not id_number.isdigit():
            raise ID_num_missing_digit(id_number)
        if check_zeros(id_number):
            if check_id_number(id_number):
                return True
            return False
    except Idtooshort:
        print(Idtooshort.__str__(id_number))
    except Idtoolong:
        print(Idtoolong.__str__(id_number))
    except ID_num_missing_digit:
        print(ID_num_missing_digit.__str__(id_number))
        
        
import itertools       
class IDIterator:
    """This class gets id number and return iterator with 10 correct id numbers,
       starts from id number that you inserted and next.
       :raise: StopIteration if total list contains more then 10 values.
       """
    def __init__(self, id_num):
        self.id_num = id_num
        self.index = -1
        self.total = []
        self.range_end = '999999999'

    def jh(self):
        for i, j in enumerate(range(int(self.id_num), 999999999)):
            if check_id_valid(str(j)):
                self.total.append(self.id_num)

            
    def __iter__(self):
        return self
   
    def __next__(self):
        if len(self.total) >= int(self.range_end) - int(self.id_num):
            raise StopIteration()
        else:
            self.index += 1
            return self.total[self.index]
        
        
        
        
        for i, j in enumerate(range(int(self.id_num), 999999999)):
            if i < 100:
                if check_id_valid(str(j)):
                    self.id_num = j
                    self.total.append(self.id_num)
                    self.index += 1
                return self.total[self.index]
            else:
                raise StopIteration()
            
#    def get_num(self):
#        for i in iter(self.total):
#            return i
#            self.id_num = i
#            while (check_id_valid(str(self.id_num))):
#                self.id_num = i
#                print(i)
#                return self.id_num   
        
        p = []
        for i, j in enumerate(range(int(self.id_num), 999999999)) :
            print(i, j)
            if (check_id_valid(str(self.id_num))):
                p.append(j)
            if i == 100:
                raise StopIteration()
        return p
    
#        y = [[num for k, num in enumerate(range(int(self.id_num), int(self.range_end))) if (check_id_valid(str(num)))] 
#        y = iter(y)
#        return y
#    
#            for i in range(int(self.id_num), int(range_end)):
#                self.id_num = i
#                if (check_id_valid(str(self.id_num))):
##                    self.total.append(self.id_num)
#                    self.index += 1
#                    return  IDIterator.get_num(self.id_num)



class IDIterator:

    def __init__(self, id_num):  
        self.id_num = id_num
        self.start = 0
        self.end = 1000000000
        self.b = 0
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.start < int(self.id_num) < self.end:
             for i, num in enumerate(range(int(self.id_num), 999999999)):
                 self.id_num = num
                 if (check_id_valid(str(self.id_num))):
                     self.b = num
                     return self.b
                 
class IDIterator:
            
    def __init__(self, id_number):  
        self._id = id_number
        self._start = 0
        self._end = 1000000000
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._start < int(self._id) < self._end:
            for i in range(int(self._id), int(self._end)):
                self._id = i    
                if check_id_valid(str(self._id)):
                    self._id += 1    
                    return self._id - 1 
        
sd = IDIterator('123456780')
print(sd.__next__())  
print(sd.__next__())  
print(sd.__next__())  


for i in sd:
    print(i)
    
#                
#        try:
#            range_end = '999999999'
#            for i in range(int(self.id_num), int(range_end)):
#                self.id_num = i
#                if (check_id_valid(str(self.id_num))):
#                    self.total.append(self.id_num)
#                if len(self.total) >= 99:
#                    self.index += 1
#                    if self.index == 99:
#                        raise StopIteration()
#                    return self.total[next(self.index)]
#        except StopIteration:
#            return
#                
                
class EmployeeManager:
    def __init__(self):
        self._employee_lst = []
        self.eml_index = -1
    def add_employee(self, new_empl):
        self._employee_lst.append(new_empl)
    def __iter__(self):
        return self
    def __next__(self):
        if self.eml_index >= len(self._employee_lst) -1:
            raise StopIteration()
        self.eml_index += 1
        return self._employee_lst[self.eml_index].get_name()            
                
                
sd = IDIterator('123456780')
#print(sd.__iter__())
print(sd.get_num())  
print(sd.__next__())  
print(sd.__next__())  
for i in sd:
    print(i)
    
iter(filter(lambda x: )

def ff(id_num):
    p = []
    for i, j in enumerate(range(int(id_num), 999999999)) :
        print(i, j)
        if (check_id_valid(str(id_num))):
            id_num = j
            p.append(id_num)
        if i == 1000:
            raise StopIteration()
    return p
                                                 
u = ff(id_num)
                
                
                
                
            
