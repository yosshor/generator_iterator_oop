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
        the id_number is too short, that means the user inserted less digits for id numbers.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
    
    def __str__(self):
        return "Your id number is too short, it must be equal to 9 numbers"
    

class Id_with_zeros(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_number is too short, that means the user inserted maybe 9 digits for id numbers but 
        with zeros at the begining they are not considered with id number.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
    
    def __str__(self):
        return "Your id number is too short, it must be equal to 9 numbers, without zeros at the begining "

    
class Idtoolong(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_number is too long, that means the user inserted more digits for id numbers.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is too long, the id number must be equal to 9 numbers"


class Num_too_high(globalException):
    """ That class inherit from globalException class for raise an exception that tells us  the id_number is 
        too high, that means the user inserted a high id number  (num that is over the edge of normal id range), 
        and the user need to insert a smaller num.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is too high, you needs to insert a num smaller then  999999700 "
    
 
    
class ID_num_missing_digit(globalException):
    """ That class inherit from globalException class for raise an exception that tells us the
        id_number is not proper, that means the user inserted letters for id numbers, and the user 
        only could insert digits.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is not proper, you need to insert only numbers" 


def check_id_valid(id_number):
    """ That function checks if the id_number is correct or proper, checks if the id number have zeros at the
        beginig, and checks if your id number is not contains only digits (for example if you have letters 
        or punctuation in your id number), and ofcourse if the length of the id number is bigger then 9 or less from 9.
        :param id_number: id_number value.
        :type id_number: str 
        :raise: Num_too_high if the id number tallest then  999999700
        :raise: Idtooshort if id_number is less then 9 digits.
        :raise: Idtoolong if id_number is more then 9 digits.
        :raise: ID_num_missing_digit if id_number not contains oonly digits.
        :raise: Id_with_zeros if id number contains zeros at the beginig.
        :return: True if the id_number contains 9 real correct digits, else raise an error and False.
        :rtype: bool 
    """
    try :
        if not id_number.isdigit():
            raise ID_num_missing_digit(id_number)  
        if str(id_number)[0] == '0':
             if len(str(int(id_number))) < 9:
                 raise Id_with_zeros(id_number)   
        if len(str(int(id_number))) < 9:
            raise Idtooshort(id_number)
        if len(str(int(id_number))) > 9:
            raise Idtoolong(id_number)
        if int(id_number) >= 999999700:
            raise Num_too_high(id_number)
            
    except Idtooshort:
        print(Idtooshort.__str__(id_number))
        return False
    except Idtoolong:
        print(Idtoolong.__str__(id_number))
        return False
    except ID_num_missing_digit:
        print(ID_num_missing_digit.__str__(id_number))
        return False
    except Id_with_zeros:
        print(Id_with_zeros.__str__(id_number))
        return False
    except Num_too_high:
        print(Num_too_high.__str__(id_number))
        return False
    else:
        return True


def check_num(id_number):
    """ This function take the correct 9 digits of id number and makes on him some manipulations, that
        means that function check if after the manipulation if the id number % 10 == 0, if yes its means 
        that id number is proper.
        :param id_number: id_number value
        :type id_number: str
        :return: True if after manipulation the id number % 10 == 0, else False.
        :rtype: bool
    """
    first = [int(j) * 2  if (i + 1) % 2 == 0 else int(j) for i, j in enumerate(str(id_number))]
    first = [str(i) for i in first]
    second = [(int(num[0]) + int(num[1]))  if int(num) > 9 else num for i, num in enumerate(first)]
    the_sum = np.sum(np.array(second, dtype = int))  # I can do it with loop and one total variable that aggregate all i in loop to the total variable
    if the_sum % 10 == 0:
        return True
    return False


class IDIterator:
    """ This class gets id number and return iterator with 10 correct id numbers,
        starts from id number that you inserted and over.
    """      
    def __init__(self, id_number):  
        self._id = id_number
        self._start = 0
        self._end = 999999999
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._start < int(self._id) < self._end:
            for i in range(int(self._id), int(self._end)):
                self._id = i    
                if check_id_valid(str(self._id)):
                    if check_num(str(self._id)):
                        self._id += 1    
                        return self._id - 1 


def id_generator(id_num):
    """ This generator function takes your impropre 9 digits id number and generat
        from that number a proper id number until it we get to 999999999.
        :param id_number: id_number value
        :type id_number: str
        :return: The next proper id number.
        :rtype: int 
    """
    for num in range(int(id_num), 999999999):
        id_num = num
        if check_id_valid(str(id_num)):
            if check_num(str(id_num)):
                yield id_num

 
def main():
    """ That is the main function, here we controll to all functions, at the beginig the user need to insert
        id number and the function runs over and over again if the id number not normal/proper (if the length
        of id_number is less from 9 digits or bigger from 9 or if its not digits) until the user insert exactly
        9 digits, and then the function check if its proper id number (if the id number contains all the conditions
        for being a proper), if the id number is proper the function will tells you that is good id number.
        :raise: StopIteretion if the function display 10 possible id proper option stop the iteration.
        :return: True if the id number is proper, else the function display to you 10 proper 
        id number options from the iterator, and 10 proper id number from generator.
        :rtype: bool 
    """
    id_number = ''
    while id_number == '':
        try:
            id_number = input("please enter the id_number : ")
            if check_id_valid(id_number):
                if check_num(id_number):
                    print("Your id number is proper")
                    raise StopIteration(id_number)
                print(" ")
                print("This 10 options for new proper id_number from iterator")
                for index, iterator in enumerate(IDIterator(id_number)):
                    if index >= 10:
                        print(" ")
                        break
                    print(iterator)
                print("This 10 options for new proper id_number from generator")
                for index_generator, generator_num in enumerate(id_generator(id_number)):
                    if index_generator >= 10:
                        raise StopIteration()
                    print(generator_num)
            main()
        except StopIteration:
            return

if __name__ == "__main__":
    main()



