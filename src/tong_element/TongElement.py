class TongElement(object):

    def __init__(self):
        self.parentElement = None
        self.nameString = None
        self.memberList = []
    
    def getKey(self):
        if self.parent == None:
            key = []
        else:
            key = self.parent.getKey()
        key.append(self.name)
        return key
