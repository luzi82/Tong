from tong_element.TongElement import TongElement
from tong_element.TongClass import TongClassMember

class TongFunc(TongClassMember):
    pass
        
class TongFuncMember(TongElement):
    pass
    
class TongFuncIn(TongFuncMember):
    def __init__(self):
        self.typeKey = None
        self.dimension = 0
        self.memberList = None
    
class TongFuncOut(TongFuncMember):
    def __init__(self):
        self.typeKey = None
        self.dimension = 0
        self.memberList = None
