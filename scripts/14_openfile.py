myfile = open('/Users/kalyansamala/Downloads/test.txt')
y = myfile.read()
print(y)
y = myfile.read()
print(y)
myfile.seek(0) #this will print nothing because curser is not at EOF. Use seek(0) to move curser to Begining of file.
y = myfile.read()
print(y)

myfile.seek(0)
z = myfile.readlines()
print(z)
