
"""
@author: Yoss
"""
# using with generator experssion

def translate(sentence):
    dictionary_words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}    
    y = (''.join(dictionary_words[word]) for word in sentence.split() if word in dictionary_words.keys())
    [print(i) for i in y]
    return 
    
translate("el gato esta en la casa")

    

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

is_prime(3)

# without using generator
def first_prime_over(n):
#    need to return the first prime number that came after n
    while not (is_prime(n)):
        n += 1
    else:
        return n
    
# using generator
def first_prime(n):
    y = (i for i in range(n, n*2) if is_prime(i))
    print(next(y))
    print(next(y))
    return

print(first_prime_over(1000000))   
first_prime(1000000)   


integers = (x for x in range(1, 12))
squared = (x for x in integers)
negated = (-y for y in squared)

for i in negated:
    print(i)
   
    
def parse_ranges(range_string):
    first_generator = (tuple(i.split('-')) for i in range_string.split(','))
    g = (num for start, stop in first_generator for num in range(int(start), int(stop)+1 ))    
    return [i for i in g]
#    next(g)
    
    
parse_ranges("1-2,4-4,8-10")
print(list(parse_ranges("0-0,4-8,20-21,43-45")))


pairs = ((1, 3),(2, 4), (5, 8))
for s, t in pairs:
    print(s,t)
#
#second_generator = [range(int(first_generator[i][0]), int(first_generator[i][1])) for i in range(len(first_generator))]
#[print(o) for o in second_generator]
#[print(p) for p in first_generator]

def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print("Enter num greader then zero")
    while count < n:
        print(n1)
        ng = n1 + n2
        n1 = n2
        n2 = ng
        count += 1
        
fibonacci(15)





def get_fibo(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print("Enter num greader then zero")
    while count < n:
        yield n1
        yield n2
        ng = n1 + n2
        n1 = n2
        n2 = ng
        count += 1

a = get_fibo(14)
for i in a:
    print(next(a))





import datetime
print(datetime.time.second)
# final
def get_sec():
    # return all the possible seconds between 0 - 59
    sec = (i for i in range(0, 60))
    return sec    
    
    
def get_minutes():
    # return all the possible minute between 0 - 59
    minutes = (i for i in range(0, 60))
    return minutes


def get_hours():
    #return the hours between 0 - 23
    hours = (i for i in range(0, 24))
    return hours



def get_time():
    hour = get_hours()
    minute = get_minutes()
    second = get_sec()
    for h in get_hours():
        for m in get_minutes():
            for s in get_sec():
                yield f"{h:02}:{m:02}:{s:02}"
                
#                time = f"{h:02}:{m:02}:{s:02}" 
#                if time == "01:23:45":
#                    break

                    


#    return (f"{h:02}:{m:02}:{s:02}" for h in hour for m in minute for s in second)


#for i in get_time():
#    print(i)



get_time()
datetime.datetime.now().year
datetime.datetime.now().second
datetime.datetime.now().month


def get_year():
    year = datetime.datetime.now().year
    while True:
        yield year
        year += 1



def get_month():
    month = datetime.datetime.now().month
    while True:
        return (mon for mon in range(0, 13))

       

def check_leaf_year(is_leaf_year):
    leaf = False
    if is_leaf_year % 4 == 0:  # or (leaf_year % 400 == 0):
        leaf = True
    if is_leaf_year % 100 == 0:
        leaf = False
    if is_leaf_year % 400 == 0:
        leaf = True
    return leaf       
        
def get_days(month, leap_year = True):
    # The generator will return how many days you have in this months
    days = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = (day for day in range(0, 32))
    elif month in [4, 6, 9, 11]:
        days = (d for d in range(0, 31))
    elif month == 2 and leap_year == True:
        days = (da for da in range(0, 30))
    else:
        days = (dayy for dayy in range(0, 29))
    return days        
  

    
import datetime  
from itertools import chain 

def get_date():
    # the generator need to return this day dd/mm/yyyy hh:mm:ss
    y = datetime.datetime.now().year
    for year in get_year():
        for month in get_month():
            for day in get_days(month, leap_year = check_leaf_year(year)):
                for i in get_time():
                    yield f"{day:02}/{month:02}/{year:04} " + str(i)
                
  
    
for i,j in enumerate(get_date()):
    if (i % 1000000 == 0):
        print(j)        


def chain_generator():
    for v in chain(get_time(), get_date()):
        print(v)
    

    


