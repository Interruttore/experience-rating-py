import os
import configparser
import constants


def createConfig():
    if (not os.path.isfile("./config.ini")):
        print("Creating config file")
        config = configparser.ConfigParser()
        config['THEME'] = {'themeName': 'DarkTeal4'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


def getConfig():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    return config


def updateConfig(section, option, value):
    if (os.path.isfile("./config.ini")):
        print("Updating config file")
        config = configparser.ConfigParser()
        config.read("./config.ini")
        config.set(section, option, value)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


def changeTheme(themeName):
    updateConfig(constants.THEME, constants.THEME_NAME, themeName)
