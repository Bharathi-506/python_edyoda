class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def sqsum(self):
        print("square sum :",self .x*self.x +self.y*self.y+self.z*self.z )
p = Point(1,3,5)
p.sqsum()
