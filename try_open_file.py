"""
author : Yossi Shor
"""

with open('new_text.txt', 'r') as p:
    print( min([l for l in p.read().split('\n')], key = len))
    print([line for line in p.read().split('\n') if len(line) == min([l for l in p.read().split('\n')], key = len)])
    print([len(line) for line in p.read().split('\n')])# if len(line) == len(sorted(p.read().split('\n'),key=len)[0])])
    print([line for line in p.read().split('\n') if len(line)==len(sorted(p.read().split('\n'),key=len)[0])])
   
    
    
print("now you import the {} script".format(__name__))
