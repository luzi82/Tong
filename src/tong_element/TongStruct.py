from tong_element.TongElement import TongElement
from tong_element.TongType import TongType
from tong_element.TongClass import TongClassMember

class TongStruct(TongClassMember, TongType):
    pass

class TongStructMember(TongElement):
    def __init__(self):
        self.typeKey = None
        self.dimension = 0
