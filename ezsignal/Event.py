import threading

from ezsignal.Signal import Signal
from ezsignal.ThreadBundle import ThreadBundle


class Event:
    def __init__(self):
        self.signal = Signal()

    def emit(self, *args):
        thread_bundle = ThreadBundle()
        remove_connections = []
        for connection in self.signal.connections:
            if not connection.is_connected:
                remove_connections.append(connection)
            else:
                thread = threading.Thread(target=connection.func, daemon=True, args=args)
                thread_bundle.add(thread)
        for connection in remove_connections:
            self.signal.connections.remove(connection)
        thread_bundle.start()
        return thread_bundle
