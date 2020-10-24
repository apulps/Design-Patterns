"""
Encapsulate a request as an object, thereby letting you parametrize clients with different requests, queue or log requests, and support undoable operations.
"""


class Invoker:
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        return sum(command.execute() for command in self._commands)


class Command:
    def execute(self):
        raise NotImplementedError("Subclass must override execute()!")


class Command1(Command):
    def __init__(self, reciever):
        self._reciever = reciever

    def execute(self):
        return self._reciever.operation()


class Reciever:
    def operation(self):
        return 1
