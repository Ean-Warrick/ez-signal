from ezsignal import Connection


class Signal:
    def __init__(self):
        self.connections = []

    def connect(self, func):
        connection = Connection(func)
        self.connections.append(connection)
        return connection
