import docker

from os import mkdir
from distutils.dir_util import copy_tree

WORKDIR = '/Users/lucasdecastro/Documents/XPROG/ContainerNet'


class BotContainer():
    STATUS_ONLINE = "bot_status_online"
    STATUS_OFFLINE = "bot_status_offline"

    def __init__(self, client, path: str, name: str, token: str):
        self.client = client
        self.container = None
        self.path = path
        self.name = 'ddx-' + name
        self.docker_context = f'{WORKDIR}/tmp/dockerfiles/{self.name}'
        self.status = self.STATUS_OFFLINE
        self.img_name = f'{self.name}_img'
        self.token = token

    def dockerize(self):
        try:
            mkdir(self.docker_context)
        except FileExistsError:
            pass

        f = open(f'{self.docker_context}/Dockerfile', 'w')
        f.write("FROM python:latest\nCOPY ./app /app \nCOPY ./requirements.txt /requirements.txt \nRUN pip install -r /requirements.txt\nCMD python /app/main.py\n")
        f.close()

        copy_tree(self.path, self.docker_context)

        self.client.images.build(path=self.docker_context, tag=self.img_name)

        try:
            self.client.containers.get(self.name).remove(force=True)
        except docker.errors.NotFound:
            pass

        self.container = self.client.containers.create(
            image=self.img_name,
            name=self.name,
            environment=[f'BOT_TOKEN={self.token}']
        )

    def start(self):
        self.container.start()

    def stop(self):
        self.container.stop()


class BotManager():
    def __init__(self) -> None:
        self.client = docker.from_env()
        self.bot_containers = {}

    def add(self, context: str, name: str, token: str):
        if (not self.bot_exists(name)):
            self.bot_containers[name] = BotContainer(
                self.client, context, name, token)
            self.bot_containers[name].dockerize()
        else:
            raise(ReferenceError(
                f"Container with name '{name}' already exists"))

    def start(self, name: str):
        if (self.bot_exists(name)):
            self.bot_containers[name].start()
        else:
            raise(KeyError(f'No container with name {name}'))

    def stop(self, name: str):
        if (self.bot_exists(name)):
            self.bot_containers[name].stop()
        else:
            raise(KeyError(f'No container with name {name}'))

    def bot_exists(self, name: str):
        return True if name in self.bot_containers.keys() else False


"""
    USAGE EXAMPLE:
        if (__name__ == "__main__"):
            bm = BotManager()
            bm.add(context=f'{WORKDIR}/bots/test',
                name='test',
                token='OTM5OTc0NzE4MDk2ODE4MTc2.YgAprA.nBwsdDhEmfOoEKHJLGvdmXwsDxg'
                )
            bm.start('test')
"""
