def my_func(param1="default"):
    """
    This is a doc string
    """
    print(f"my first python function {param1}")
    
my_func()

def hello():
    return "hello"

result = hello()
print(result)

def addNum(num1, num2):
    return num1 + num2

# Lambda Expression

# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(list(evens))

#lambda
evens = filter(lambda num: num%2 == 0, mylist)
print(list(evens))

#split method
tweet = "Go sports! #Sports and go"
result = tweet.split("#")[1]
print(result)


