#Takes arguments, does not return a value
'''
def print_sum(a, b):
    print(a + b)

print_sum(34,6)
'''
#Takes argument returns a value
'''
def sum(a, b):
    return a + b
balance = 0
income = 1000
balance += sum(balance, income)
print(balance)
'''

# called "say_hello" that take no arguments, prints hello, returns nothing
def say_hello():
    print("Hello")
    
say_hello()

# called "say hello to" that takes a name, prints "hello {name}", returns nothing
def  say_hello_to(name):
    print("Hello {}". format(name))
    
say_hello_to("Chair")

# called 'double' that takes an integer as an argument, and returns double its value
def double(n):
    return n * 2

assert double(4) == 8

# called "last_first" that takes a irst name and a last name.
# it will return the name in the format (last_name, first_name)

def last_first(first_name, last_name):
     return "{}, {}". format(last_name, first_name)
 
assert last_first("Mickey", "Mouse") == "Mouse, Mickey"
