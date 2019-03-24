try:
    for i in ['a','b','c']:
        print(i**2)

except:
    print("Error occured")


x = 5
y = 0
try:
    z = x/y

except:
    print("Error occured")

finally:
    print("All Done")