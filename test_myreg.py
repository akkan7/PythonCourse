import unittest
from MyReg import myreg
import numpy as np


class MyReg_test(unittest.TestCase):
        def test_input(self):
            with self.assertRaises(AttributeError):
                myreg(1, 1)
            with self.assertRaises(ValueError):
                x= np.array((1,2,3,"name"))
                y=np.array((3,4,5))
                myreg(x,y)

        def test_lengtherror(self):
            x = np.random.randint(10, size=(10, 3))
            y = np.random.randint(10, size=(15, 1))
            with self.assertRaises(ValueError):
                myreg(x,y)




if __name__ == '__main__':
    unittest.main()
