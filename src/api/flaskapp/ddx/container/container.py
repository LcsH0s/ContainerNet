import docker

from distutils.dir_util import copy_tree
from os import mkdir


class AppContainer():
    STATUS_ONLINE = "bot_status_online"
    STATUS_OFFLINE = "bot_status_offline"

    def __init__(self, client, path: str, name: str, token: str):
        self.client = client
        self.container = None
        self.path = path
        self.name = name
        self.ctn_name = 'ddx-' + name
        self.docker_context = f'/tmp/dockerfiles/{self.ctn_name}'
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
            self.client.containers.get(self.ctn_name).remove(force=True)
        except docker.errors.NotFound:
            pass

        self.container = self.client.containers.create(
            image=self.img_name,
            name=self.ctn_name,
            environment=[f'BOT_TOKEN={self.token}'],
            network_mode='bridge',
            auto_remove=True)

    def start(self):
        self.container.start()
        self.status = self.STATUS_ONLINE

    def stop(self):
        self.container.stop()
        self.status = self.STATUS_OFFLINE

    def is_running(self) -> bool:
        if (self.container.status == 'running'):
            return True
        return False
