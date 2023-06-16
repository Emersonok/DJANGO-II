#Exercise 1
s = "django"

#Use indexing to print out the ff
#"d"
print(s[0])
#"o"
print(s[-1])
#"djan"
print(s[0:4])
#jan
print(s[1:4])
#go
print(s[-2:])

#Bonus: Use indexing to reverse the string
print(s[::-1])
    

#Exercise 2

l = [3,7,[1,4,"hello"]]
#reassing hello to goodbye

l[2][2] = "goodbye"
print(l)

#exercise 3

#grab the hellos
d1 = {"simple": "hello"}
print(d1["simple"])

d2 = {"k1": {"k2": "hello"}}
print(d2["k1"]["k2"])

d3 = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
print(d3["k1"][0]["nest_key"][1][0])

#exercise 4
#Use a set to find the unique values

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

set_list = set(mylist)
print(set_list)


#exercise 5
age = 4
name = "Sammy"
print(f"Hello my dog's name is {name} and he is {age} years old")

# print("Hello my dog's name is {a} and he is {b} years old".format(a=name, b=age))

