try:
    f = open("simple.txt", "r")
    f.write("Test write to simple text!")
except IOError:
    print("Error: File not found")
# else:
#     print("Success")
#     f.close()
finally:
    print("Always function no matter")
    
