"""
Primitive
    Boolean
    Numbers
    Strings
"""
num1 = 42 # Numbers
num2 = 2.3 # Numbers
boolean = True # Boolean

"""
List 
    initialize
    access value
    change value
    add value
    delete value
Tuples
    initialize
    access value
    change value
    add value
    delete value
Dictionary
    initialize
    access value
    change value
    add value
    delete value
"""
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary
fruit = ('blueberry', 'strawberry', 'banana') # Tuples

print(type(fruit)) # Tuples: Access value html
print(pizza_toppings[1]) # List: Access value
pizza_toppings.append('Mushrooms') # Add value
print(person['name']) # Dictionary: Access value
person['name'] = 'George' # Dictionary: Change value
person['eye_color'] = 'blue' # Dictionary: Change value
print(fruit[2]) # tuples: Access value

pizza_toppings.pop() # List: Delete value
pizza_toppings.pop(1) # List: Delete value

print(person) #Initialize
person.pop('eye_color') # Delete value
print(person) #Initialize

"""
conditional
    if
    else if
    else
"""
if num1 > 45: # if
    print("It's greater")
else: # else
    print("It's lower")

if len(string) < 5: # if
    print("It's a short word!")
elif len(string) > 15: # else if
    print("It's a long word!")
else: # else
    print("Just right!")

"""
for loop
    start
    stop
    increment
    break
    continue
    sequence
"""
for x in range(5): # Start:0, Stop:5
    print(x)
for x in range(2,5): # Start:2, Stop:5
    print(x)
for x in range(2,10,3): # Start:2, Stop:10, Increment:3
    print(x)
for topping in pizza_toppings: 
    if topping == 'Pepperoni':
        continue # Continue
    print('After 1st if statement')
    if topping == 'Olives':
        break # Break

""""
while loop
    start
    stop
    increment
"""
x = 0 # Start:0
while(x < 5): # Stop:5
    print(x)
    x += 1 # Increment:1

""""
function
    parameter
    argument
    return
"""
def print_hello_ten_times():
    for num in range(10): # Stop:10
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # Parameter:x
    for num in range(x): # Stop:x
        print('Hello')

print_hello_x_times(4) # Argument:4

def print_hello_x_or_ten_times(x = 10): # Parameter:x = 10
    for num in range(x): # Stop:10
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4) # Argument:4


"""
Bonus section
"""

print(num3) # NameError: name <variable name> is not defined
num3 = 72
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) # KeyError: 'favorite_team'
print(pizza_toppings[7]) # IndexError: list index out of range
print(boolean) # IndentationError: unexpected indent
fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
