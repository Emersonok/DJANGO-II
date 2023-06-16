mystring = "abc def"
print(mystring[0])
print(mystring[-1])

#Slicing
print(mystring[:-1])

print(mystring[::2])
print(mystring[3])

#split
up = mystring.split()
print(up)

#Format

X = "Item One: {}, Item two".format("dog", "cat")
print(X)

#Lists

mylist = ["a", "b", "c", "d", "e"]
listtwo = ["x", "y", "z"]

mylist.extend(listtwo)
print(mylist)
mylist.extend(["f", "g"])
print(mylist)
mylist.pop(0)
print(mylist)
mylist.reverse()
print(mylist)

numlist = [1, 3, 0, 54, 43, 19, 5]
numlist.sort()
print(numlist)

newlist = [1, 2, ["x", "y", "z"]]
print(newlist[2][1])

#List comprehension
matrix = [[1,2,3], [4,5,6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)
