from collections import OrderedDict

d = OrderedDict()
d[10]='A'
d[11]='B'
d[12]='C'
d[13]='D'

for i,j in d.items():
    print(i,j)

#l1 = [1,2,3]
#l2 = [3,4,5]

'''lst = [i*j for i in l1 for j in l2]
print(lst)'''


#num3 = [i+j for i in l1 for j in l2]
#print(num3)

#num3 = [i for i in l1 if i not in l2]
#rint(num3)



#Using Dictionaries
#dict = {'Pratap':1000, 'Vishnu': 20000}
#dict3 = dict.copy()

#dict2 = {value: key for key,value in dict.items()}
#print(dict2)


#for key,value in dict.items():
 #   print(f"{key} value is {value}")

#for key in dict.keys():
#    print(key)


#for values in dict3.values():
#    print(values)


'''dict1 = {}

elements = int(input("Elements: "))

for i in range(elements):
    print("Enter the key: ", end = '')
    key = input()

    print("Enter the value: ", end ='')
    value = int(input())
    print('\n')

    dict1.update({key:value})


#original dictionary
print("Original dictionary is ", dict1)
print('\n')
print('\n')
print('\n')

for key,value in dict1.items():
    print(f"The key is {key} and the value is {value}")

#finding the keys or values from dict1
#print(dict1.get("Vishnu",-1))


#chaging from dict to list
print(list(dict1))


#how to handle duplicate keys in dictionary
dict2 = {}
for k ,v in dict1.items():
    if k in dict1:
        dict2[k]+=',' +v
    else:
        dict2[k] = v'''




#find how many times a word is repeated in a string
'''string = "Indranil"

dict = {}

for x in string:
    dict[x] = dict.get(x,0)+1


for key,value in dict.items():
    print(f'({key}:{value})', end=',')'''




#sorting the dictionaries using lambdas
'''colours = {10:"red", 35:"Green", 15:"Yellow", 25:"Blue"}
print(sorted(colours.items(), key = lambda t:t[0], reverse = True))

print(sorted(colours.items(), key = lambda t:t[1], reverse = True))'''

'''countries = ["USA","India","Germany","France"]
cities = ["Washington","Delhi","Berlin","Paris"]

z = zip(countries, cities)
d = dict(z)

print(d)'''



'''string = "Vijay =23, Ganesh = 24, Laskhmi=34"
lst = []

for x in string.split(','):
    y = x.split('=')
    lst.append(y)

d=dict(lst)

d1 = {}
for k,v in d.items():
    d1[k] = int(v)

print(d1)
print(lst)'''









