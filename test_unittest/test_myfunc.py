import unittest
import numpy as np
from myfunc import add,sub
import pdb

class TestMyFunc(unittest.TestCase):#inherits from class unittest.TestCase
    def setUp(self):
        print("prepare the test environment before test")

    def tearDown(self):
        print("after executation tear down the env")
    
    def test_add(self):
        print('add')
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2))
    def test_sub(self):
        print('sub')
        self.assertEqual(-1,sub(1,2))
        self.assertNotEqual(3,add(2,2))
        a=np.random.randint(-100,100,(3,5))
        b=np.random.randint(-100,100,(3,5))
        c=a+b
#        pdb.set_trace()
        self.assertEqual(c,add(a,b))
        self.assertEqual(2*c,add(a,b))

if __name__=='__main__':
    unittest.main()

