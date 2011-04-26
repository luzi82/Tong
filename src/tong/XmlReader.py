import xml.parsers.expat 
from tong_element.TongClass import TongClass
import os.path
from tong_element.TongFunc import TongFuncIn, TongFuncOut, TongFunc

class XmlReader:
    
    def __init__(self):
        self.file = None
        self.success = False
        self.resultClass = None
        self.stateList = []
        self.elementDict = dict()
        self.elementList = []
    
    def setFile(self, file):
        self.file = file
    
    def process(self):
        p = xml.parsers.expat.ParserCreate()
        p.StartElementHandler = self.start_element
        p.EndElementHandler = self.end_element
        p.CharacterDataHandler = self.char_data
        self.stateList.append(InitState())
        self.stateList[0].reader = self
        p.ParseFile(open(self.file, "rb"))
        for e in self.elementList:
            if e.getKey() in self.elementDict:
                raise Exception(e.getKey + " dup")
            self.elementDict[e.getKey()] = e
        self.success = True;

    def start_element(self, name, attrs):
        print('Start element:', name, attrs)
        oldState = self.stateList[-1]
        newState = oldState.child(name, attrs)
        if newState == None :
            raise Exception (oldState.__class__.__name__, name, attrs)
        newState.reader = self
        newState.parent = oldState
        newState.set(name, attrs)
        self.stateList.append(newState)

    def end_element(self, name):
        print('End element:', name)
        oldState = self.stateList[-2]
        newState = self.stateList[-1]
        output = newState.output();
        self.elementList.append(output)
        oldState.input(output)
        self.stateList.pop()

    def char_data(self, data):
        print('Character data:', repr(data))

class XmlReaderState(object):
    
    def __init__(self):
        self.name = None
        self.attrs = None
        self.reader = None
        self.parent = None
        self.me = None
    
    def set(self, name, attrs):
        self.name = name
        self.attrs = attrs
        if "name" in attrs:
            self.me.nameString = attrs["name"]
    
    def child(self, name, attrs):
        return None
    
    def char(self, data):
        pass
    
    def input(self, childOutput):
        childOutput.parentElement = self.me
        self.me.memberList.append(childOutput)

    def output(self):
        return self.me


class InitState(XmlReaderState):
    
    def child(self, name, attrs):
        if name == "class":
            return ClassState()
        
    def input(self, childOutput):
        self.reader.resultClass = childOutput
        

class ClassState(XmlReaderState):
    
    def __init__(self):
        self.me = TongClass()
    
    def set(self, name, attrs):
        super().set(name, attrs)
        self.me.nameString = os.path.basename(self.reader.file).split(".")[0]

    def child(self, name, attrs):
        if name == "func":
            return FuncState()
        

class FuncState(XmlReaderState):
    
    def __init__(self):
        self.me = TongFunc()

    def child(self, name, attrs):
        if name == "in":
            return FuncInState()
        elif name == "out":
            return FuncOutState()
        

class FuncInState(XmlReaderState):
    
    def __init__(self):
        self.me = TongFuncIn()

    def set(self, name, attrs):
        super().set(name, attrs)
        self.me.typeKey = attrs["type"]
        if "dimension" in attrs:
            self.me.dimension = attrs["dimension"]
        

class FuncOutState(XmlReaderState):

    def __init__(self):
        self.me = TongFuncOut()

    def set(self, name, attrs):
        super().set(name, attrs)
        self.me.typeKey = attrs["type"]
        if "dimension" in attrs:
            self.me.dimension = attrs["dimension"]
