class Email:

    def __init__(self,fromAddress,toAddress,cc,bcc,subject,body):

        self.__fromAddress = fromAddress
        self.__toAddress = toAddress
        self.__cc = cc
        self.__bcc = bcc
        self.__subject = subject
        self.__body = body

    def GetFromAddress(self):
        return self.__fromAddress[1]
    
    def GetToAddress(self):
        return self.__toAddress[1]

    def GetCc(self):
        return self.__cc[1]

    def GetBcc(self):
        return self.__bcc[1]

    def GetSubject(self):
        return self.__subject

    def GetBody(self):
        return self.__body