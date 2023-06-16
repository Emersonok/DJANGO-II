#problem 1
def array_check(nums):
    for i in range(len(nums)-2):
        
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

check = array_check([1, 1, 2, 1, 2, 3])
print(check)


#problem 2
def stringBits(mystring):
    newstring = ""
    for i in range(len(mystring)):
        if i%2 == 0:
            newstring += mystring[i]
            
    return newstring

strings = stringBits("Hello")
print(strings)

#problem 3
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    
    # return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-(len(a)):]

word = end_other("Hiabc", "abc")
print(word)

#problem 4

def doubleChar(mystring):
    result = ""
    for char in mystring:
        result += char*2
    return result

char = doubleChar("you")
print(char)

#problem 5

def no_teen_sum (a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n== [13, 14, 17, 18, 19]:
        return 0
    return n
    

teens = no_teen_sum(2, 13, 1)
print(teens)

#problem 6

def count_evens(nums):
    
    # count = 0
    
    # for item in nums:
    #     if item % 2 == 0:
    #         count += 1
            
    # return count
    # even = []
    # for item in nums:
    #     if item % 2 == 0:
    #         even.append(item)
            
    # return len(even)
    even = [item for item in nums if item %2 == 0 ]
    return len(even)

num = count_evens([2, 10, 3, 2, 6, 5, 8, 10])
print(num)

 



