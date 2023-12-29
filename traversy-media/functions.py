# Function is block of code which only runs when it is called

# Create function
def sayHello(name):
    print(f'Hello {name}')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


# A lambda function is a small ana\onymous function. Can take any number of arguments, but can have only one expression. Similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2 

print(getSum(10, 3))