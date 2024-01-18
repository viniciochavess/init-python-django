listNumber = [2,4,1,2,444,33,2]
listNumberDoble = [number * 2 for number in listNumber]
print(listNumberDoble) #[4, 8, 2, 4, 888, 66, 4]

number = [2,3, 4, 1]
number.append(2) #[2, 3, 4, 1, 2]

print(number)
number.insert(2,300) #[2, 3, 300, 4, 1, 2]
print(number)
number.pop() #[2, 3, 300, 4, 1]
print(number)
del(number[3]) #[2, 3, 300, 1]
print(number)
number.remove(3) #[2, 300, 1]
print(number)
number.clear() #[]
print(number)