import docker

from os import mkdir
from . import error
from ..container import container


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
        try:
            self.get_bot_by_name(name).start()
        except error.BotReferenceError as e:
            raise(e('Impossible to start bot '))

    def stop(self, name: str) -> None:
        if (self.bot_exists(name)):
            if (self.bot_containers[name].status == container.AppContainer.STATUS_RUNNING):
                self.bot_containers[name].stop()
            else:
                raise(error.BotStatusError("bot is not running"))
        else:
            raise(KeyError(f'No container with name {name}'))

    def bot_exists(self, name: str) -> bool:
        return True if name in self.bot_containers.keys() else False

    def get_online_bots(self) -> list:
        return [bot.name for bot in self.bot_containers.values() if bot.status == container.AppContainer.STATUS_RUNNING]

    def get_bot_by_name(self, name: str) -> container.AppContainer:
        if (self.bot_exists(name) and self.bot_containers[name].is_container_valid()):
            return self.bot_containers[name]
        raise(error.BotReferenceError(f'No container with name \'{name}\''))
