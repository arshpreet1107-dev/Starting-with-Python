fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

fruits.sort()                
fruits.insert(1, "cherry")   
fruits.append("grapes")      
fruits.remove("banana")      
popped_item = fruits.pop()   
fruits.reverse()             
print( fruits)
print(len(fruits))
print( popped_item)



print("List items using loop:")
for fruit in fruits:
    print( fruit)
print("apple" in fruits)
