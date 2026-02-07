list1 = ['apple', 'banana', 'cherry']
list2 = [1, 2, 3]
list3 = [True, False, True]
list4 = ['abc', 1, True, 40, 'male']

#type
myList = ['apple', 'banana', 'cherry',"orange", "kiwi", "melon", "mango"]
print(type(myList))

#access the item
print(myList[0])

#ranges of index
print(myList[2:5])


#list Constructor
thisList = list(('apple', 'banana', 'cherry'))
print(thisList)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])