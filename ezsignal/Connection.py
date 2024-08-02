class Connection:
    def __init__(self, func):
        self.is_connected = True
        self.func = func
