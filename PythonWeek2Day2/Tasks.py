#2nd commitssss

Shop_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print(Shop_list)
print(type(Shop_list))
print(Shop_list[0])
print(Shop_list[-1])
Shop_list[1] = "rice"
print(Shop_list)
Shop_list.append("carrots")
print(Shop_list)
smallList = ["toffee", "coffee"]
Shop_list.extend(smallList)
print(Shop_list)
Shop_list.remove("bananas")
print(Shop_list)
Shop_list.pop()
print(Shop_list)

print(Shop_list[1:3])
print(Shop_list[0::2])
print(Shop_list[:-3:-1])

stud1 = {"name": "susan",
         "stream": "tech",
         "lessonCount": 4,
         "lessons": ["variables", "dataTypes", "set up"]
         }
print(stud1)
print(type(stud1))
print(stud1["stream"])
print(stud1["lessons"][0])
stud1["lessonCount"] = 3
stud1["lessons"].remove("dataTypes")
print(stud1)
print(stud1.keys())

fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits.add("orange")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.add("apple")
print(fruits)
s = {1, 2, 3}
for element in fruits:
    print(element)
# sets dont index

# frozen set is an immutable

