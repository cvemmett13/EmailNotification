import imapclient
import pyzmail
import Python.EmailNotification.EmailClass as EmailClass


class ImapConnection:

    imaplib._MAXLINE = 10000000

    def __init__(self,server,emailAddress,password,readOnlyFlag):
        self.__server = server
        self.__emailAddress = emailAddress
        self.__password = password
        self.__readOnlyFlag = readOnlyFlag

    # set the folder to search
    def SetFolder(self,folder):
        self.__folder = folder

        self.__serverConnection.select_folder(self.__folder,readonly = self.__readOnlyFlag)

    # decide whether to mark the emails as read or not
    # true is readonly which does not mark as read
    def SetReadOnlyFlag(self,readOnlyFlag):
        self.__readOnlyFlag = readOnlyFlag

        self.__serverConnection.select_folder(self.__folder,readonly = self.__readOnlyFlag)
    
    def GetReadOnlyFlag(self):
        return self.__readOnlyFlag

    def ConnectToServer(self,email,password):

        # create the imap object
        self.__serverConnection = imapclient.IMAPClient(self.__server, ssl=True)

        # login to the server
        self.__serverConnection.login(self.__emailAdress, self.__password)

    def SearchFolder(self,searchParameters):

        # returns a list of id #s for emails
        return self.__serverConnection.search(searchParameters)
    
    def GetEmail(self, UID):

        # fetch the raw message from the server
        self.__rawMessage = self.__serverConnection.fetch(UID,['BODY[]'])

        # create a pyzmail object from the raw message
        self.__message = pyzmail.PyzMessage.factory(self.__rawMessage['BODY[]'])

        textBody = ""

        # pull the text body if it exists or the html body
        # if the text body does not exist
        if self.__message.text_part != None:
            textBody = self.__message.text_part.get_payload().decode(self.__message.text_part.charset)

        if self.__message.html_part != None and textBody == "":
            body = self.__message.html_part.get_payload().decode(self.__message.html_part.charset)

        else:
            body = textBody

        # create email object instance
        self.__email = EmailClass.Email(
            self.__message.get_addresses('from'),
            self.__message.get_addresses('to'),
            self.__message.get_addresses('cc'),
            self.__message.get_addresses('bcc'),
            self.__message.get_subject,
            body)


        return self.__email