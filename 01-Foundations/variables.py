
name= input("Enter your name: ")
print("Hello " + name)
age = int(input("Enter your age: "))
print("Your age is: ", age)

if age>=18:
    print("You are eligible to vote")

print("Trying new end line.", end=' ')
print("Here is new line")
print(3)
print("some text", 5+9, "Again some text")


x=4
x='nn'
print(x)

#Variable
x=str("hello")
print(x)
y=3
print(type(x))
print(type(y))



x,y,z='test','d','e'
print(x)
print(y)
print(z)
x=y=z='hh'
print(z)

fruits=['apple', 'banana', 'orange']
x,y, z=fruits
print(x)

a="awesome"

def my_func():
    #global a
    a='perfect'
    print("You are " + a)
my_func()
print("You are " +a)


x='awesome'
print(x[3])

s='hi'
print(2*s)


name= input("Enter your name: ")
print(f"hello, {name}")




# age=input("Enter age")
# age=int(age)
# print(f"you aeg is :{age}")
#
#
# lines=[]
# for i in range(1):
#     line=input("Enter line")
#     lines.append(i)
#
# print("You entered")
# for line in lines:
#     print(line)