import json
import os

# filepath 'C:\\Users\\Charl\\OneDrive\\Documents\\Programming\\Python\\EmailNotification\\config.json'

class Configuration:

    def __init__(self,filepath):
        self.__filepath = filepath
        
        config = open(self.__filepath)

        config = config.read()

        self.__config = json.loads(config)

    def GetTwilioSid(self):

        return self.__config['config']['Twilio']['AccoundSid']
    
    def GetTwilioAuthToken(self):

        return self.__config['config']['Twilio']['AuthToken']

    def GetTwilioNumber(self):

        return self.__config['config']['Twilio']['TwilioNumber']

    def GetSendNumber(self):

        return self.__config['config']['Twilio']['SendNumber']

    def GetAccountNames(self):

        return self.__config['config']['Accounts']