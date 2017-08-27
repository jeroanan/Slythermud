class Room(object):

    def __init__(self):
        self.__id = "-1"
        self.__name = ""
        self.__description = ""

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,val):
        self.__id = val
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def description(self):
        return self.__description
        
    @description.setter
    def description(self, val):
        self.__description = val
