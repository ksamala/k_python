name = "Venkateshwar_rao"
age = 2
r = 0.123456789
print(f"This is {name} and age is {age}") 
print(f"First letter of {name} is {name[0]}") # String index Syntax: name[0][1][2]....
print(f"Last letter of {name} is {name[-1]}") 
# We can find last letter of a string whose lenth is unkownusing -ve numbers, Syntax: name[0][-1][-2][-3]
print(f"{name[0:5:2]}") # Syntax: "string[start:stop:jump]"
print(f"{name[0:16:3]}")
print(f"{name[::-1]}") # Reverse String
name = name.upper()
print(f"{name}")
name = name.split('E') #Here field seperator is E
print(f"{name}") 

#obersve output, values depending on index values.
print('The {} {} {}'.format('quick','brown','fox'))
print('The {1} {2} {0}'.format('quick','brown','fox'))
print('The {0} {0} {0}'.format('quick','brown','fox'))
print('The {q} {b} {f}'.format(q= 'quick',b= 'brown',f= 'fox'))
print("The float  value is{v:6.3f}".format(v=r)) #{value:width.percision f}.format(value=result)
print(f"The float  value is{r:6.3f}")
