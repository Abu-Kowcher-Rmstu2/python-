#taking input in python using input().
#input() read input as string. we need to convert it to int, float etc.

a = input("enter a string : ")
print(a)
print("the type of {} is {} : ".format(a,type(a)))

#taking integer as input.
x = int(input("enter an integer value: "))
print(type(x))

#taking float as input.
x = float(input("enter a float value: "))
print(type(x))

### taking multiple value at same time using input().split().
"""
split(seperator, maxsplit) uses two argument. seperator is space by default. you can specify other separators such as comma,hyphen
etc. to take input.
"""
b,c,d = [int(x) for x in input("enter three integers: ").split()]

print("the value of b,c,d is ",b, " ",c," ",d)

###taking array as input separated by comma
arr = []
arr = [int(x) for x in input("enter an array of elements: ").split(",")]

print(arr)

### taking list of input
name = list(map(int, input("enter the items of list : ").split()))

print(name)
