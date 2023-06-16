mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)
    
for (tup1, tup2) in mypairs:
    print(tup1)
    print(tup2)
    
print(list(range(0,20,2)))

for item in range(10):
    print(item)
    
#list comprehension

x = [1,2,3,4]
# out = []
# for num in x:
#     out.append(num**2)
    
# print(out)

out = [num**2 for num in x]
print(out)

nums = [1, 1, 2, 1, 2, 3]
for i in range(len(nums)-1):
    print(i)
