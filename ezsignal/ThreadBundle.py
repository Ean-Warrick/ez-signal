class ThreadBundle:
    def __init__(self):
        self.threads = []
        self.is_running = False
        self.is_dead = False

    def add(self, thread):
        self.threads.append(thread)