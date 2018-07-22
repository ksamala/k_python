mynumlist = [3,2,1]
print(mynumlist)

mynumlist.sort() #sort list
my_sorted_list = mynumlist
print(mynumlist)

mynumlist.reverse() #reverse list
my_rev_list = mynumlist
print(mynumlist)

mylist = ['kalyan',26,60.5,26]
print(mylist)

conc_list = mylist + mynumlist #concatinate
print(conc_list)

l = len(mylist)
print(l)

mylist.append('04/02') #add element to list
print(f"{mylist}")

mylist.pop() #pop off last element in list
print(f"{mylist}")

mylist.pop(0) #pop off using index number
print(f"{mylist}") 
