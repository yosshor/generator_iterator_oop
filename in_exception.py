# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:48:42 2020

@author: EGLOBAL
"""

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
    
    
    
    
    
    
    
    
    
    
    
