# List Comprehension can utilize conditional statement to modify existing list.
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

#Nested If with list comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 ==0]
print(num_list)

#If .... else  With list comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)