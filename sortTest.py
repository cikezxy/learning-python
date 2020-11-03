fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits)) #['apple', 'banana', 'grape', 'raspberry']
print(sorted(fruits, reverse=True)) #['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits,key=len)) #['grape', 'apple', 'banana', 'raspberry']
# sorted不改变原数组
print(fruits) #['grape', 'raspberry', 'apple', 'banana']

# list.sort是原为排序，会改变原数组
fruits.sort()
print(fruits) #['apple', 'banana', 'grape', 'raspberry']