
import subprocess


class Bot():
    def __init__(self, token:str, name:str, path:str) -> None:
        self.token = token
        self.path = path
        self.name = name
        self.thread


class BotManager():
    def __init__(self) -> None:
        self.bots = []
        self.activeBots = []
        self.offlineBots = []
    
    def add(self, name:str, path:str, token:str) -> None:
        self.bots.append(Bot(token,name, path))
    
    def start(self, name:str) -> None:
        if (self.getBotbyName(name) != None):
            bot:Bot = self.getBotbyName(name)
            bot.thread = subprocess.Popen(['/bin/bash', 'python3 /bots/test/main.py'])
        
    
    def getNames(self) -> list:
        print([b.name for b in self.bots])
        return [b.name for b in self.bots]
    
    def getBotbyName(self, name:str) -> Bot:
        for b in self.bots:
            if (b.name == name):
                return b
        return None