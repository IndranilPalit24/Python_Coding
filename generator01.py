def generatorworker(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
    
number = generatorworker(10)
number = generatorworker(10)


for i in number:
    print(i, end=",")
    