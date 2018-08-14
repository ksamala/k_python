import math

class Line:    
    def A(self):
        self.x1 = int(input("Enter X1 co-ordinate "))
        self.y1 = int(input("Enter Y1 co-ordinate "))
        self.x2 = int(input("Enter X2 co-ordinate "))
        self.y2 = int(input("Enter Y2 co-ordinate "))
        return self.x1,self.y1,self.x2,self.y2

    def distance(self):
        self.x_dist = self.x2-self.x1
        self.y_dist = self.y2-self.y1
        d2 = math.sqrt((self.x_dist ** 2) + (self.y_dist ** 2))
        print(f"Distance between points is ",d2)
       
    def slope(self):
        m = self.y_dist / self.x_dist
        print(f"Slope is {m}")

x = Line()
x.A()
dist = x.distance()
slpe = x.slope()