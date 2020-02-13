# -*- coding: utf-8 -*-
"""
@author: Yossi
"""

#This the first file call it file1
class GreetingCard:
    def __init__(self, _recipient = 'Dana Ev', _sender = 'Eyal Ch'):
        self._recipient = _recipient
        self._sender = _sender
    
    def greeting_msg(self):
        return f"the sender is {self._sender} and the recipient is {self._recipient}"

#GreetingCard().greeting_msg()
    

#This a new file call it file2
from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self, _sender = 'Eyal Ch', _recipient = 'Dana Ev', _sender_age = 0):
        GreetingCard.__init__(self, _sender, _recipient)
        self._sender_age = _sender_age

    def greeting_msg(self):
        return f"Happy birthday {self._sender} and {self._recipient} the sender age is {self._sender_age}"

# its the file
from file1 import GreetingCard
from file2 import BirthdayCard

A = GreetingCard()
B = BirthdayCard()

print(A.greeting_msg())
print(B.greeting_msg())

#GreetingCard().greeting_msg()    
    
#BirthdayCard().get_age()
    