import json
import os

thisDir = os.getcwd()

x = open('C:\\Users\\Charl\\OneDrive\\Documents\\Programming\\Python\\EmailNotification\\config.json')

x = x.read()

y = json.loads(x)



for account in ((y['config']['Accounts']['Account'])):

    print(account[])