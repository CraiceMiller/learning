# function = A block of reusable block
# place () after the funtion name to invoke it 
# to invoke the funtion you need to type ()
# it is like a pair of telephones talking to each other

# look modules.py file :) 

# name
def birthday(name:str, age:int):
     return f'happy birthday {name.capitalize()}, and {age}!!, your are really getting old'
    



# dispaly
def display_invoice(username, amount, due_date):
    print(f'hello {username.capitalize()}')
    print(f"your bill of ${amount:.2f} is due: {due_date}")
    print()



#  return = statement used to end a function 
# and send a result back to the caller
def add(x, y):
    z = x + y
    return z


# create a full name
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + '' + last



def full_name(nam, las):
    nam = nam.capitalize()
    las = las.capitalize()
    return nam + ' ' + las



def name(name):
    a = name.lstrip().lower().capitalize()
    return a

    
def numbers(l, m):
    k = l + m
    return k


