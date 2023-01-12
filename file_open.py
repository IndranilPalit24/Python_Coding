'''f = open('file1.txt','r')
print(f.read())
f.close()'''



'''try:
    f = open('file1.txt','r')
    print(f" Cursor position is {f.tell()}")
    print(f.read())

except FileNotFoundError:
    print("File is not found")

finally:
    print(f"cursor position is {f.tell()}")
    f.close()'''


'''f = open('file1.txt','r')
print(f"Cursor Position is {f.tell()}")
print(f.read())
print('\n')

print("before seek")
print(f.seek(0))

print('\n')
print("after seek")

print(f"Cursor position is {f.tell()}")
print(f.read())
f.close()'''




'''try:
    with open('file1.txt') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("Not found")

finally:
    f.close()'''


'''try:
    f = open(r"D:\LearnCoding\newfile.txt")
    print(f.read())
except FileNotFoundError:
    print("File is not found")

finally:
    f.close()'''


try:
    with open('file1.txt','r+') as f:
        print(f.read())
        f.seek(len(f.read()))
        f.write("Message is still simple if we want wars we want wars")

except FileNotFoundError:
    print('Not found')

finally:
    f.close()

