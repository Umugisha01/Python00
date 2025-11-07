a = {'name' : 'john', 'age' :20}
b = {'name': 'May', 'age': 23}
customers = {'c1': a, 'c2': b}

for x, obj in customers.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])



# thisdict = {
#     "brand": "Ford",
#     "model": "Mystang",
#     "electric": False,
#     "year": 1964
# }


# for x in thisdict:
#     print(f"{x}: {thisdict[x]}")

# for x in thisdict.values():
#     print(x)

# for x in thisdict.keys():
#     print(x)

# for x, y in thisdict.items():
#     print(x, y)
# 
# thisdict.pop("model")
# thisdict.popitem()
# del thisdict["model"]

# print(thisdict)


# thisdict["year"] = 2018

# thisdict.update({"year": 2020})
# print(thisdict.items())

# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary!")

# x = thisdict.keys()

# print(x)

# thisdict["color"] ="white"

# print(x)

# w = thisdict.values()

# print(w)

# thisdict["year"] = 2020

# print(w)

# x = thisdict.items()
# thisdict["year"] = 2020
# print(x)



# x = thisdict["model"]
# print(x)

# y = thisdict.get("brand")
# print(y)

# v = thisdict.keys()
# print(v)

# print(thisdict["model"])