from tong_element.TongElement import TongElement
from tong_element.TongType import TongType, TongTypeKey

class TongStruct(TongElement, TongType):
    pass

class TongStructMember(TongElement):
    def __init__(self):
        self.typeKey = TongTypeKey()
        self.dimension = 0
