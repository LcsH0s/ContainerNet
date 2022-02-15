import docker

from os import mkdir
from ..error.error import error
from ..container.container import container


class ContainerManager():
    def __init__(self) -> None:
        self.client = docker.from_env()
        self.bot_containers = {}
        try:
            mkdir(f'/tmp/dockerfiles')
        except FileExistsError:
            pass

    def add(self, context: str, name: str, token: str) -> None:
        if (not self.bot_exists(name)):
            self.bot_containers[name] = container.AppContainer(
                self.client, context, name, token)
            self.bot_containers[name].dockerize()
        else:
            raise(ReferenceError(
                f"Container with name '{name}' already exists"))

    def start(self, name: str) -> None:
        if (self.bot_exists(name)):
            self.bot_containers[name].start()
        else:
            raise(KeyError(f'No container with name {name}'))

    def stop(self, name: str) -> None:
        if (self.bot_exists(name)):
            if (self.bot_containers[name].status == container.AppContainer.STATUS_ONLINE):
                self.bot_containers[name].stop()
            else:
                raise(error.BotStatusError("bot is not running"))
        else:
            raise(KeyError(f'No container with name {name}'))

    def bot_exists(self, name: str) -> bool:
        return True if name in self.bot_containers.keys() else False

    def get_online_bots(self) -> list:
        return [bot.name for bot in self.bot_containers.values() if bot.status == container.AppContainer.STATUS_ONLINE]

    def get_bot_by_name(self, name: str) -> container.AppContainer:
        if (self.bot_exists(name)):
            return self.bot_containers[name]
        raise(KeyError(f'No container with name \'{name}\''))
