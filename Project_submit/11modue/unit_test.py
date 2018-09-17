class calc:

      def mul_num(self,a,b):
          num1 = int(a)
          num2 = int(b)
          return a*b


      def  div_num(self,a,b):
           num1 = int(a)
           num2 = int(b)
           return a/b


import unittest
class Testcalc(unittest.TestCase):

      def test_mult(self):
       c = calc()
       res = c.mul_num(2,6)
       self.assertEqual(12,res)

      def test_multi(self):
       c = calc()
       res = c.mul_num(2,6)
       self.assertNotEqual(11,res)

      def test_div(self):
          c = calc()
          res = c.div_num(6,2)
          self.assertEqual(3,res)

      def test_divi(self):
          c = calc()
          res = c.div_num(6,2)
          self.assertNotEqual(2,res)

      def test_intt(self):
         c = calc()
         res = c.mul_num(2,3)
         self.assertEqual(6,res)

      def test_intg(self):
         c = calc()
         res = c.mul_num(2,3)
         self.assertEqual(6,res)
         res1 = c.div_num(res,2)
         self.assertEqual(3,res1)


      def test_integ(self):
         c = calc()
         res = c.mul_num(2,3)
         res1 = c.div_num(res,2)
         self.assertNotEqual(2,res1)



if __name__ == '__main__':
          print("This is the unit test results")
          unittest.main()
