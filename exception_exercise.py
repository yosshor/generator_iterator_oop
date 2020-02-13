# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 19:51:03 2019

@author: EGLOBAL
"""
# some of exception 

def stop_iteration(s):
    g = iter(s)
    print(next(g))
    print(next(g))

def zero_division(num):
    return num / 0

import torch

def indetation_erorr(f):
    r = f
           print(r)
  
def assertion_error(w):
    assert w == 1
    return w

def import_error(r):
    print('import ' + str(r))
    import r

def ioerror(l):
    r =print(l,'r')
    r.close()

def keyerror(t):
    # keyerror rise up when its not in dictionary
    r = {'jim' : 12, 'yossi' : 13 }
    return r[t]



def syntaxerror():
    print ""
    
    
def type_error(e):
    return e * 2
    
    
    
stop_iteration('e')
zero_division(12)
assertion_error('e')
import_error('torch')
ioerror('yoss')
keyerror('jim')
print""   #syntax_error

indetation_erorr('d')

type_error()





try:
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    print("The result is: " + str(number_1 / number_2))
except ZeroDivisionError:
    print("Cannot divide the provided input.")
except ValueError:
    print("Invalid input was provided, please provide integers only!")


def read_file(file_name):
    try:
        print("__CONTENT_START__")
        f = open(file_name, 'r')
    except :
        print("__NO_SUCH_FILE__")
    else :
        print("This is the content from the file")
        [print(i) for i in f.readlines()]
        return
    finally :
        print("__CONTENT_END__")
        return
    
print(read_file('new_text.txt'))   
    
    
    

def read_file(file):
    try :
#        f = open(file, 'r')
#        print([i for i in f.read().split()])
        print('__CONTENT_START__')

        with open(file, 'r') as f:
            r = [i for i in f.readlines()]
            print(r)
            
#            print([i for i in f.readlines()])
           
    except IOError as s:
        print('__NO_SUCH_FILE__')
#        print('cant open this file', s)
    except OSError as d:
        print('you enter invalid syntaxs', d)
    except FileNotFoundError as error:
        print('__NO_SUCH_FILE__')
    else:
        f.close()
    finally:
         print('__CONTANT_END__')
        
          
        
read_file('new_text.txt')      




    
    
class UnderAge(Exception):
    def __init__(self, age):
        self.age = age
        
    def __str__(self):
        return "your age {} is under the exceptable, and you needs to wait {} years \
    until you can come to the ido party".format(self.age, 18 - self.age)

    def get_age(self):
        return self.age

UnderAge(122).__str__()



def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    #        print('under age')
            
    except UnderAge as s:
        print(UnderAge(age).__str__())
    
    else:
        print('you should send an invite to :', name)

send_invitation('Yossi Shor', 19)
























