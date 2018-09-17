
#creating circle class using properties and different methods


class circlearea( ):
       pi = 3.14

       def  __init__(self,radius):
             self.radius = radius

       @property
       def areaofcircle(self):
           return  self.pi*self.radius*self.radius

       def __add__(self,radius2):
           self.radius2 =  radius2
           return self.pi*2*(self.radius+self.radius2)

       def __cmp__(self,radius3):
           self.radius3 = radius3
           return self.radius>self.radius3

       def __gt__(self,radius4):
           self.radius4 = radius4
           return self.radius >self.radius4

       def __lt__(self,radius5):
           self.radius5 = radius5
           return self.radius <self.radius4

       def __eq__(self, radius5):
           self.radius5 = radius5
           return self.radius == self.radius5

       def __repr__(self,radius):
           return f"Circle with radius: {self.radius}"

       def __str__(self,radius):
           return f"Circle with radius: {self.radius}"




c =circlearea(4)
k =c.areaofcircle
print(k)
k1 = c.__add__(5)
print(k1)
k2 = c.__cmp__(2)
print(k2)
k3 = c.__gt__(5)
print(k3)
k4 = c.__lt__(7)
print(k4)
k5 = c.__eq__(5)
print(k5)
k7 =c.__repr__(5)
print(k7)
k6= c.__str__(5)
print(k6)

import unittest
class Testmail(unittest.TestCase):

    def test_areaequal(self):
        t1 = circlearea(4)
        r1 = t1.areaofcircle
        self.assertEqual(r1, 50.24)

    def test_areanotequal(self):
        t1 = circlearea(5)
        r1 = t1.areaofcircle
        self.assertNotEqual(r1, 78)

    def test_addequal(self):
        t2 = circlearea(4)
        r2 = t2.__add__( 5)
        self.assertEqual(r2, 56.52)

    def test_addnotequal(self):
        t2 = circlearea(4)
        r2 = t2.__add__( 5)
        self.assertNotEqual(r2, 232)




if __name__ == '__main__':
    unittest.main()
