# DICTIONARY METHODS: keys(), values(), items(), get(), update()
info = {
    "name": "Md Asif",
    "class": "Warrior",
    "level": 87,
    "attributes": ["fire", "earth", "wind"]
}


# keys = (info.keys())
# keys = list(info.keys()) 
# Can be Typecasted to List
# Note: keys(), values(), and items() return view objects (not plain lists)

# print(keys) 
# displays all keys
# print(type(keys)) 
# displays the type


# values = info.values()
# print(type(values), values) 
# displays the type of the variable values and the values from the info

# print(info)
# print(info.items()) 
#note the difference here

# print (info["class2"]) 
# #Gives a KeyError if the key is missing
# print ("END OF CODE")

# print (info.get("class2")) 
# #Returns None if the key is missing

# if ((info.get("class2")) == "None"):
#     print()
# else:
#     print ("END OF CODE")

# update() merges new key-value pairs into the existing dictionary.
info.update({
    "weakness": "water"
})

# items() returns a view of the dictionary's key-value pairs.
print(info.items())