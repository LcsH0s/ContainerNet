import docker
import os


class botContainer():
    def __init__(self, path:str, name:str):
        self.client = docker.from_env()
        self.path = path
        self.name = name
        self.img_name = f'{self.name}_img'
        self.client.images.build(path=self.path, tag=self.img_name)
        self.container = self.client.containers.create(self.img_name)
        
    def start()

client = docker.from_env()
client.images.build(path="/Users/lucasdecastro/Documents/XPROG/ContainerNet/tmp/dockerfiles/music_test", tag="ouiouiouioui")
print("Started")
lol = client.containers.create("ouiouiouioui")
lol.start()
print("oui")
lol.stop()
print("stoped")