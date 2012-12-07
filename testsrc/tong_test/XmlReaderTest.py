'''
@author: luzi82
'''
import unittest
from tong.XmlReader import XmlReader
from tong_element.TongClass import TongClass
from tong_element.TongFunc import TongFunc
from tong_element.TongFunc import TongFuncIn, TongFuncOut
from tong_element.TongStruct import TongStruct, TongStructMember


class XmlReaderTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_func(self):
        xr = XmlReader()
        xr.setFile("testcase/func/c0.xml")
        xr.process()

        resultClass = xr.resultClass
        self.assertTrue(isinstance(resultClass, TongClass))
        self.assertEqual(xr.elementDict["c0"],resultClass)
        self.assertNotEqual(resultClass.memberList, None)
        self.assertEqual(resultClass.nameString, "c0")
        self.assertEqual(resultClass.parentElement, None)
        self.assertEqual(len(resultClass.memberList), 9)
        
        func = xr.resultClass.memberList[0]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f0"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f0")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 0);
        
        func = xr.resultClass.memberList[1]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f1"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f1")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 0);

        func = xr.resultClass.memberList[2]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f2"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f2")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertEqual(xr.elementDict["c0.f2.a0"],fin)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement, func)
        self.assertEqual(fin.typeKey, "txt")
        self.assertEqual(fin.dimension, 0)

        func = xr.resultClass.memberList[3]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f3"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f3")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertEqual(xr.elementDict["c0.f3.a0"],fin)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement,func)
        self.assertEqual(fin.typeKey, "int")
        self.assertEqual(fin.dimension, 0)

        func = xr.resultClass.memberList[4]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f4"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f4")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 2);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertEqual(xr.elementDict["c0.f4.a0"],fin)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement,func)
        self.assertEqual(fin.typeKey, "txt")
        self.assertEqual(fin.dimension, 0)
        fin = func.memberList[1]
        self.assertNotEqual(fin, None)
        self.assertEqual(xr.elementDict["c0.f4.a1"],fin)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a1")
        self.assertEqual(fin.parentElement,func)
        self.assertEqual(fin.typeKey, "int")
        self.assertEqual(fin.dimension, 0)

        func = xr.resultClass.memberList[5]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f5"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f5")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fout = func.memberList[0]
        self.assertNotEqual(fout, None)
        self.assertEqual(xr.elementDict["c0.f5.o0"],fout)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertEqual(fout.typeKey, "txt")
        self.assertEqual(fout.dimension, 0)

        func = xr.resultClass.memberList[6]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f6"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f6")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 1);
        fout = func.memberList[0]
        self.assertNotEqual(fout, None)
        self.assertEqual(xr.elementDict["c0.f6.o0"],fout)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertEqual(fout.typeKey, "int")
        self.assertEqual(fout.dimension, 0)

        func = xr.resultClass.memberList[7]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f7"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f7")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 2);
        fout = func.memberList[0]
        self.assertNotEqual(fout, None)
        self.assertEqual(xr.elementDict["c0.f7.o0"],fout)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertEqual(fout.typeKey, "txt")
        self.assertEqual(fout.dimension, 0)
        fout = func.memberList[1]
        self.assertNotEqual(fout, None)
        self.assertEqual(xr.elementDict["c0.f7.o1"],fout)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o1")
        self.assertEqual(fout.parentElement,func)
        self.assertEqual(fout.typeKey, "int")
        self.assertEqual(fout.dimension, 0)

        func = xr.resultClass.memberList[8]
        self.assertNotEqual(func, None)
        self.assertEqual(xr.elementDict["c0.f8"],func)
        self.assertTrue(isinstance(func, TongFunc))
        self.assertEqual(func.nameString, "f8")
        self.assertEqual(func.parentElement, resultClass)
        self.assertNotEqual(func.memberList, None)
        self.assertEqual(len(func.memberList), 4);
        fin = func.memberList[0]
        self.assertNotEqual(fin, None)
        self.assertEqual(xr.elementDict["c0.f8.a0"],fin)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a0")
        self.assertEqual(fin.parentElement,func)
        self.assertEqual(fin.typeKey, "txt")
        self.assertEqual(fin.dimension, 0)
        fin = func.memberList[1]
        self.assertNotEqual(fin, None)
        self.assertEqual(xr.elementDict["c0.f8.a1"],fin)
        self.assertTrue(isinstance(fin, TongFuncIn))
        self.assertEqual(fin.nameString, "a1")
        self.assertEqual(fin.parentElement,func)
        self.assertEqual(fin.typeKey, "int")
        self.assertEqual(fin.dimension, 0)
        fout = func.memberList[2]
        self.assertNotEqual(fout, None)
        self.assertEqual(xr.elementDict["c0.f8.o0"],fout)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o0")
        self.assertEqual(fout.parentElement,func)
        self.assertEqual(fout.typeKey, "txt")
        self.assertEqual(fout.dimension, 0)
        fout = func.memberList[3]
        self.assertNotEqual(fout, None)
        self.assertEqual(xr.elementDict["c0.f8.o1"],fout)
        self.assertTrue(isinstance(fout, TongFuncOut))
        self.assertEqual(fout.nameString, "o1")
        self.assertEqual(fout.parentElement,func)
        self.assertEqual(fout.typeKey, "int")
        self.assertEqual(fout.dimension, 0)
        
        self.assertEqual(len(xr.elementDict),22)
        self.assertEqual(len(xr.elementList),22)

    def test_struct(self):
        xr = XmlReader()
        xr.setFile("testcase/struct/c0.xml")
        xr.process()
        
        resultClass = xr.resultClass
        self.assertTrue(isinstance(resultClass, TongClass))
        self.assertEqual(xr.elementDict["c0"],resultClass)
        self.assertNotEqual(resultClass.memberList, None)
        self.assertEqual(resultClass.nameString, "c0")
        self.assertEqual(resultClass.parentElement, None)
        self.assertEqual(len(resultClass.memberList), 8)

        mem = xr.resultClass.memberList[0]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s0"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s0")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 0);

        mem = xr.resultClass.memberList[1]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s1"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s1")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 0);

        mem = xr.resultClass.memberList[2]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s2"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s2")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 1);
        memm = mem.memberList[0]
        self.assertNotEqual(memm, None)
        self.assertEqual(xr.elementDict["c0.s2.m0"],memm)
        self.assertTrue(isinstance(memm, TongStructMember))
        self.assertEqual(memm.nameString, "m0")
        self.assertEqual(memm.parentElement, mem)
        self.assertEqual(memm.typeKey, "txt")
        self.assertEqual(memm.dimension, 0)

        mem = xr.resultClass.memberList[3]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s3"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s3")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 1);
        memm = mem.memberList[0]
        self.assertNotEqual(memm, None)
        self.assertEqual(xr.elementDict["c0.s3.m0"],memm)
        self.assertTrue(isinstance(memm, TongStructMember))
        self.assertEqual(memm.nameString, "m0")
        self.assertEqual(memm.parentElement, mem)
        self.assertEqual(memm.typeKey, "int")
        self.assertEqual(memm.dimension, 0)

        mem = xr.resultClass.memberList[4]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s4"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s4")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 2);
        memm = mem.memberList[0]
        self.assertNotEqual(memm, None)
        self.assertEqual(xr.elementDict["c0.s4.m0"],memm)
        self.assertTrue(isinstance(memm, TongStructMember))
        self.assertEqual(memm.nameString, "m0")
        self.assertEqual(memm.parentElement, mem)
        self.assertEqual(memm.typeKey, "txt")
        self.assertEqual(memm.dimension, 0)
        memm = mem.memberList[1]
        self.assertNotEqual(memm, None)
        self.assertEqual(xr.elementDict["c0.s4.m1"],memm)
        self.assertTrue(isinstance(memm, TongStructMember))
        self.assertEqual(memm.nameString, "m1")
        self.assertEqual(memm.parentElement, mem)
        self.assertEqual(memm.typeKey, "int")
        self.assertEqual(memm.dimension, 0)

        mem = xr.resultClass.memberList[5]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s5"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s5")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 1);
        memm = mem.memberList[0]
        self.assertNotEqual(memm, None)
        self.assertEqual(xr.elementDict["c0.s5.m0"],memm)
        self.assertTrue(isinstance(memm, TongStructMember))
        self.assertEqual(memm.nameString, "m0")
        self.assertEqual(memm.parentElement, mem)
        self.assertEqual(memm.typeKey, "c0.s0")
        self.assertEqual(memm.dimension, 0)

        mem = xr.resultClass.memberList[6]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s6"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s6")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 1);
        memm = mem.memberList[0]
        self.assertNotEqual(memm, None)
        self.assertEqual(xr.elementDict["c0.s6.m0"],memm)
        self.assertTrue(isinstance(memm, TongStructMember))
        self.assertEqual(memm.nameString, "m0")
        self.assertEqual(memm.parentElement, mem)
        self.assertEqual(memm.typeKey, "txt")
        self.assertEqual(memm.dimension, 1)

        mem = xr.resultClass.memberList[7]
        self.assertNotEqual(mem, None)
        self.assertEqual(xr.elementDict["c0.s7"],mem)
        self.assertTrue(isinstance(mem, TongStruct))
        self.assertEqual(mem.nameString, "s7")
        self.assertEqual(mem.parentElement, resultClass)
        self.assertNotEqual(mem.memberList, None)
        self.assertEqual(len(mem.memberList), 1);
        memm = mem.memberList[0]
        self.assertNotEqual(memm, None)
        self.assertEqual(xr.elementDict["c0.s7.m0"],memm)
        self.assertTrue(isinstance(memm, TongStructMember))
        self.assertEqual(memm.nameString, "m0")
        self.assertEqual(memm.parentElement, mem)
        self.assertEqual(memm.typeKey, "c0.s0")
        self.assertEqual(memm.dimension, 1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
