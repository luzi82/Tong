class TongElement(object):

    def __init__(self):
        self.parentElement = None
        self.nameString = None
        self.memberList = []
    
    def getKey(self):
        if self.parentElement == None:
            return self.nameString
        else:
            return self.parentElement.getKey()+"."+self.nameString
