import Python.EmailNotification.EmailClass as EmailClass
import Python.EmailNotification.EmailInterface as EmailInterface
import Python.EmailNotification.TextMessage as TextMessage
import Python.EmailNotification.Configuration as Configuration

def main():

    config = Configuration('config.json')

    loginEmail = config.GetLoginEmail