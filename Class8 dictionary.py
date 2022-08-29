#in a python dictionary data is stored in a key and value {key:value}
#dictionary is ordered, changeable but does not allow key duplication
thisdict = {
    "brand":"toyota",
    "model":"camry",
    "year": 2018,
    "owner":"Zoe Odia"
}
#print(thisdict)
#to print individual items in a dictionary
#print(thisdict["model"])
#print(thisdict["year"])
#print(thisdict["brand"])
#print(thisdict["owner"])

#print(len(thisdict))
#result = thisdict["model"]
#result = thisdict.get("model")
all_my_keys = thisdict.keys()
#print(all_my_keys)

#To add or change items in a dictionary
thisdict["colour"] = "blue"
thisdict["owner"] = "Ayemere"
#print(thisdict)

#print(type(all_my_keys))

all_my_values = thisdict.values()
#print(all_my_values)

dict_cont = thisdict.items()
#print(dict_cont)

#for (key,value) in thisdict.items():
    #print(key, value)

#thisdict["ride"] = "yes"
#if "ride" in thisdict:
   # print(thisdict["ride"])
#else:
   # print("key does not exist")

#thisdict.update({"owner":"jay","ride":2020})
#print(thisdict)
#thisdict.pop("ride")
#print(thisdict)
#thisdict.popitem()
#print(thisdict)
thisdict.clear()
print(thisdict)

