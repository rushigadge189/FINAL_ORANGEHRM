import configparser

config = configparser.RawConfigParser() ;

filepath= "D:\PYTHON CT15\OrangeHRM\configuraton\config.ini" ;

config.read(filepath) ;

class Readconfig():

    @staticmethod
    def GetUserName():
        username=config.get("common data", "Username") ;
        return username ;

    def GetPassword():
        password=config.get("common data", "Password") ;
        return password ;