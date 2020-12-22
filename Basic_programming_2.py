#Creating a simple function to add some numbers
def summation(l1):
    return sum([i for i in l1])

list1 = []
for i in range(int(input())):
    list1.append(int(input()))
print(summation(list1))

#Creation of a dictionary and also to showcase the key value pairs
dict1 = {'Apples':5,'Oranges':8,'Patties':20,'Soda':4,'Cigarrettes':20,'Beer':6}
for i in dict1.keys():
    print('{}:{}'.format(i,dict1[i]))

#Adding new values to a dictionary:
dict1['Glasses'] = 3
print(dict1)

#Replacing the value of a prexisting value in the dictionary:
dict1['Beer'] = 10
print(dict1)

#Removing a key value pair in dictionary:
dict1.pop('Cigarrettes')
if 'Cigarrettes' in dict1:
    print('You are at a risk of lung cancer')
else:
    print('Good Choice')