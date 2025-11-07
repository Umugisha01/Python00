thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
tropical = ["hello", "pineapple", "papaya"]
fruits = ["apple", "Watermelon", "papaya"]
numbers = [1, 10, 6, 7, 2, 3, 90, 35, 12, 35, 20, 8]
numbers02 = [20, 10, 30, 60, 70]


# numbers.extend(numbers02)
# numbers03 = numbers + numbers02
# for x in numbers02:
#     numbers.append(x)

# print (numbers)
#COPY LISTS
# mynumbers = numbers.copy()
# print(mynumbers)

# myFruits = list(fruits)
# print(myFruits)

# myList = thislist[:]
# print(myList)


#sorting
# fruits.sort(key = str.lower)
# print (fruits)

# def myfunc(n):
#     return abs(n - 50)

# numbers.sort(key = myfunc)
# print(numbers)

# numbers.sort(reverse = True)
# print(numbers)

# thislist.sort()
# print(thislist)

# List Comprehension

# newlist = [x if x != "papaya" else "orange" for x in fruits]

# newlist = [x.upper() for x in fruits]

# newlist = ["hello" for x in fruits]
# print (fruits)

# newlist = [x for x in thislist if 'a' in x]

# newlist = [x for x in thislist]
# x = 0
# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# for x in thislist:
#     if "a" in x:
#         newlist.append(x)



# for x in thislist:
#     print(x)

# print("\n")
# for a in range(len(thislist)):
#     print(thislist[a])
# print("\n")
# i = 0
# while i < len(thislist):
#     print(f"{thislist[i]}")
#     i+=1

# [print(b) for b in thislist]



# print(thislist)

# thislist[1] = "blackcurrant"
# thislist[1:3] = ["banana", "watermelon"]
# thislist.extend(tropical)

# thislist.remove("apple")
# thislist.pop(3)
# del thislist[0]
# thislist.clear()


# thislist.append("coconut")
# thislist.insert(0, "vine")

# print(thislist[-4:-1])
# if "Apple" in thislist:
#     print ("Yes, 'apple' is in the fruit list!")
# else:
#     print ("Sorryt the fruit is not in the fruit list!")

