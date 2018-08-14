class Cylinder():
    
    def __init__(self,height=3,radius=4):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*(3.14)*self.radius*self.height)
 
volu = Cylinder(2,4)
print(volu.volume())
print(volu.surface_area())