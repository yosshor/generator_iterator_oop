# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:12:35 2019

@author: EGLOBAL
"""
import string

class globalException(Exception):
    def __init__(self, username):
        self.username = username
    
    def __str__(self):
        return "its depand on your exception"
    
    def get_username(self):
        return self.username



class Usernamecontainsillegalcharacter(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self, char, index):
        return "The username contains an illegal character {} at index {}".format(char, index)



class Usernametooshort(globalException):
    def __init__(self, username):
        globalException.__init__(self, username)
    
    def __str__(self):
        return "your user name is too short, it must be greater then 3 letters"
    
    

class Usernametoolong(globalException):
    def __init__(self, username):
        globalException.__init__(self, username)
        
    def __str__(self):
        return "your user name is too long, the user name must be small then 16 characters"
    
    

class Passwordmissingcharacter(Exception): 
    def __init__(self, password):
        self.password = password
#        globalException.__init__(self, password)
    
    def __str__(self):
        return " The password is missing a character "
    
    def get_password(self):
        return self.password



class password_missing_uppercase(Passwordmissingcharacter):
    def __init__(self, password):
        Passwordmissingcharacter.__init__(self, password)
    def __str__(self):
        return Passwordmissingcharacter(password).__str__() + str('Uppercase')

class password_missing_lowercase(Passwordmissingcharacter):
    def __init__(self, password):
        Passwordmissingcharacter.__init__(self, password)
    def __str__(self):
        return Passwordmissingcharacter(password).__str__() + str('Lowercase')
    
class password_missing_punctuation(Passwordmissingcharacter):
    def __init__(self, password):
        Passwordmissingcharacter.__init__(self, password)
    def __str__(self):
        return Passwordmissingcharacter(password).__str__() + str('Special')

class password_missing_digit(Passwordmissingcharacter):
    def __init__(self, password):
        Passwordmissingcharacter.__init__(self, password)
    def __str__(self):
        return Passwordmissingcharacter(password).__str__() + str('Digit')



class Passwordtooshort(Exception): 
    def __init__(self, password):
        self.password = password
#        globalException.__init__(self, password)
        
    def __str__(self):
        return "your passwordis too short, it must be greater than 8"



class Passwordtoolong(Exception):
    def __init__(self, password):
        self.password = password
#        globalException.__init__(self, password)
    
    def __str__(self):
        return " your password greater than 40 characters, nad it must be lower than that"
    
    

def check_input_for_username(some_input):
    flag_digit = False
    flag_alpha = False
    flag_punctuation = False
    for i in some_input:
        if i.isdigit():
            flag_digit = True
        if i.isalpha():
            flag_alpha = True
        if i == '_' and i !=string.punctuation :
            flag_punctuation = True
    t = [print(Usernamecontainsillegalcharacter(some_input).__str__(i, some_input.find(i))) for i in some_input if i in string.punctuation and i != '_']
    return flag_alpha and flag_digit and flag_punctuation


def check_input_for_password(some_input):
    flag_digit = False
    flag_alpha_upper = False
    flag_alpha_lower = False
    flag_punctuation = False
    for i in some_input:
        if i.isdigit():
            flag_digit = True
        if i.islower():
            flag_alpha_lower = True
        if i in string.punctuation:
            flag_punctuation = True
        if i.isupper():
            flag_alpha_upper = True        
    return flag_alpha_lower and flag_alpha_upper and flag_digit and flag_punctuation


def check_username(some_input):
    flag_digit = False
    flag_alpha = False
    flag_punctuation = False
    for i in some_input:
        if i.isdigit():
            flag_digit = True
        if i.isalpha():
            flag_alpha = True
        if i == '_' and i !=string.punctuation :
            flag_punctuation = True       
    return flag_alpha and flag_digit and flag_punctuation


def tell_the_wrong_password(password):
    flag_digit = False
    flag_alpha_upper = False
    flag_alpha_lower = False
    flag_punctuation = False
    for i in password:
        if i.isdigit():
            flag_digit = True
        if i.islower():
            flag_alpha_lower = True
        if i in string.punctuation:
            flag_punctuation = True
        if i.isupper():
            flag_alpha_upper = True 
    if not flag_digit:
        print(password_missing_digit(password))
    if not flag_alpha_upper:
        print(password_missing_uppercase(password))
    if not flag_alpha_lower:
        print(password_missing_lowercase(password))
    if not flag_punctuation:
        print(password_missing_punctuation(password))


def check_input(username, password): 
    try:
        if check_username(username) and check_input_for_password(password):
            print("OK")

        if len(username) < 3:
            raise  Usernametooshort(username)
            
        if len(username) > 16:
            raise Usernametoolong(username)

        if len(password) > 40:
            raise Passwordtoolong(password)    
    
        if len(password) < 8:
            raise Passwordtooshort(password)
      
        if not check_input_for_password(password):
            tell_the_wrong_password(password)
            
#        if check_username(username):
#            t = [print(Usernamecontainsillegalcharacter(username).__str__(i, username.find(i))) for i in username if i in string.punctuation and i != '_']
#            return   

    except  Usernametooshort:
        print(Usernametooshort.__str__(username))
        
    except Usernametoolong:
        print(Usernametoolong.__str__(username))
        
    except Passwordmissingcharacter:
        print(Passwordmissingcharacter.__str__(password))
        
    except Passwordtooshort:
        print(Passwordtooshort.__str__(password))
     
    except Passwordtoolong:
        print(Passwordtoolong.__str__(password))

    else :
        if check_username(username):
            t = [print(Usernamecontainsillegalcharacter(username).__str__(i, username.find(i))) for i in username if i in string.punctuation and i != '_']
            return
     
      
def main():    
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

if __name__ == "__main__":
    main()

