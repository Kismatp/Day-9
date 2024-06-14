# --------------wap to create a class rectangle, class methods area() and perimeter and use them by creating an instace of rectanle 
class Rectangle:
        Length=  0.0
        Breadth= 0.0 
        def __init__ (self,Length,Breadth):
            self.Length=Length
            self.Breadth= Breadth
        def calculate_area(self):
            self.area=self.Length*self.Breadth
        def calculate_perimeter(self):
             self.peri= 2*(self.Length+self.Breadth)

rect1= Rectangle(100,200)
rect1.calculate_area()
rect1.calculate_perimeter()
print("The area of rect1 is: ", rect1.area)
print("The perimeter of rect1 is: ",rect1.peri)



