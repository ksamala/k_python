class Name():
    def __init__(self, hyd, knr):
        self.hyderabad = hyd
        self.karimnagar = knr

my_name = Name(hyd = 'town', knr = 'city')

print(f'Hyderabad is {my_name.hyderabad}')
print(f'Karmimnagar is {my_name.karimnagar}')



class Name2():

    def __init__(se, India, Japan, USA):
        se.Ind_attribute = India
        se.Jap_attribute = Japan
        se.US_attribute = USA


my_name2 = Name2('Rupee','Yen','Dollar')

print(f'name is {my_name2.Ind_attribute}')
print(f'name is {my_name2.Jap_attribute}')
print(f'name is {my_name2.US_attribute}')