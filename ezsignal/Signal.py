import threading

from ezsignal import Connection
from ezsignal import ThreadBundle

class Signal:
    def __init__(self):
        self.connections = []

    def connect(self, func):
        connection = Connection(func)
        self.connections.append(connection)
        return connection

    def emit(self, *args):
        thread_bundle = ThreadBundle()
        for connection in self.connections:
            if not connection.is_connected:
                self.connections.remove(connection)
            else:
                thread = threading.Thread(target=connection.func, daemon=True)
                thread_bundle.add(thread)
        thread_bundle.start()
        return thread_bundle

