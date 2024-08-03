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
        remove_connections = []
        for connection in self.connections:
            if not connection.is_connected:
                remove_connections.append(connection)
            else:
                thread = threading.Thread(target=connection.func, daemon=True, args=args)
                thread_bundle.add(thread)
        for connection in remove_connections:
            self.connections.remove(connection)
        thread_bundle.start()
        return thread_bundle

