from tong_element.TongElement import TongElement
from tong_element.TongType import TongType

class TongStruct(TongElement, TongType):
    pass

class TongStructMember(TongElement):
    def __init__(self):
        self.typeKey = None
        self.dimension = 0
