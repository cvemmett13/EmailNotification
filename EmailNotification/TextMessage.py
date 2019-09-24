class TextMessage:

    def __init__(self, emailObject):
        
        self.__emailObject = emailObject

    def BuildTextMessage(self):

        self.__textMessage = ('You have received an important email.',
        '\n\nFrom:',self.__emailObject.GetFromAddress(),
        '\n\nSubject:',self.__emailObject.GetSubject(),
        '\n\nBody:',self.__emailObject.GetBody())

        return self.__textMessage