# string and conditional statements:

print("hello"+"world")
str1="this is a string.\nthis is me"
str2="khushi surana"
str3="this is my 'second' class of python"
print(str1)

#escape sequence characters
#\n is for next line

# concatenation
print(str1+str2+str3)

#length of string ( counts spaces also)

print(len(str2))

#indexing (starts with 0)
print(str1[1])

#slicing:

print(str2[0:6]) #includes 1st but not 6th
#hushi
print(str2[0:len(str2)])

print(str2[0:])

#negative indexing(starts with -1 : -1,-2,-3 backwards)
print(str2[-4:-1])

#.endswith

print(str2.endswith("ana"))
print(str2.endswith("pna"))

#.capitalize
print(str2.capitalize())

str2=str2.capitalize()
print(str2)

#.replace
print(str2.replace("Khushi","bhagya"))

#.find
print(str2.find("h"))
print(str2.count("a"))
print(str2)

# 
name=input("enter your name:")
print("length of name",len(name))

print(str2)

# #Conditional Statements:
# #if,elif,else

# #syntax means right form of writing codes in python

age=18
if(age>19):
    print("wrong")
elif(age<19):   
    print(" u r wrong")

#traffic case:
light="pink"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("stop")
else:
    print("light is broken")

age=24
if(age>18):
    print("can vote")
else:
    print("cannot vote")

marks=45
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
elif(marks<70):
    print("D")

#NESTING:

age=98

if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# check whether a no. is even or odd:

number=int(input("enter the number="))

rem= number % 2   # this sign % is for taking out remainder
if(rem==0):
    print("even")
else:
    print("odd")



