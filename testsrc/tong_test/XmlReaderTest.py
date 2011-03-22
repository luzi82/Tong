'''
Created on 2011年3月21日

@author: luzi82
'''
import unittest
from tong.XmlReader import XmlReader
from tong_element.TongClass import TongClass
from tong_element.TongFunc import TongFunc
from tong_element.TongFunc import TongFuncIn, TongFuncOut


class XmlReaderTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_func(self):
        xr = XmlReader()
        xr.setFile("testcase/func/c0.xml")
        xr.process()
        xr.success = True

        resultClass = xr.resultClass
        self.assertTrue(isinstance(resultClass, TongClass))
        self.assertNotEqual(resultClass.memberList, None)
        self.assertEqual(resultClass.nameString, "c0")
        self.assertEqual(resultClass.parentElement, None)
        self.assertEqual(len(resultClass.memberList), 9)
        
        func = xr.resultClass.memberList[0]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f0")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 0);
        
        func = xr.resultClass.memberList[1]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f1")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 0);

        func = xr.resultClass.memberList[2]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f2")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement, func)
        self.assertSequenceEqual(fin.typeKey, ["txt"])
        self.assertEqual(fin.dimension, 0)

        func = xr.resultClass.memberList[3]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f3")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement,func)
        self.assertSequenceEqual(fin.typeKey, ["int"])
        self.assertEqual(fin.dimension, 0)

        func = xr.resultClass.memberList[4]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f4")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 2);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement,func)
        self.assertSequenceEqual(fin.typeKey, ["txt"])
        self.assertEqual(fin.dimension, 0)
        fin = func.memberList[1]
        self.assertNotEqual(fin, None)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a1")
        self.assertEqual(fin.parentElement,func)
        self.assertSequenceEqual(fin.typeKey, ["int"])
        self.assertEqual(fin.dimension, 0)

        func = xr.resultClass.memberList[5]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f5")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fout = func.memberList[0]
        self.assertNotEqual(fout, None)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertSequenceEqual(fout.typeKey, ["txt"])
        self.assertEqual(fout.dimension, 0)

        func = xr.resultClass.memberList[6]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f6")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fout = func.memberList[0]
        self.assertNotEqual(fout, None)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertSequenceEqual(fout.typeKey, ["int"])
        self.assertEqual(fout.dimension, 0)

        func = xr.resultClass.memberList[7]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f7")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 2);
        fout = func.memberList[0]
        self.assertNotEqual(fout, None)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertSequenceEqual(fout.typeKey, ["txt"])
        self.assertEqual(fout.dimension, 0)
        fout = func.memberList[1]
        self.assertNotEqual(fout, None)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o1")
        self.assertEqual(fout.parentElement,func)
        self.assertSequenceEqual(fout.typeKey, ["int"])
        self.assertEqual(fout.dimension, 0)

        func = xr.resultClass.memberList[8]
        self.assertNotEqual(func, None)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f8")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 4);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement,func)
        self.assertSequenceEqual(fin.typeKey, ["txt"])
        self.assertEqual(fin.dimension, 0)
        fin = func.memberList[1]
        self.assertNotEqual(fin, None)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a1")
        self.assertEqual(fin.parentElement,func)
        self.assertSequenceEqual(fin.typeKey, ["int"])
        self.assertEqual(fin.dimension, 0)
        fout = func.memberList[2]
        self.assertNotEqual(fout, None)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertSequenceEqual(fout.typeKey, ["txt"])
        self.assertEqual(fout.dimension, 0)
        fout = func.memberList[3]
        self.assertNotEqual(fout, None)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o1")
        self.assertEqual(fout.parentElement,func)
        self.assertSequenceEqual(fout.typeKey, ["int"])
        self.assertEqual(fout.dimension, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
