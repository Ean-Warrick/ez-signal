import threading


class ThreadBundle:
    def __init__(self):
        self.threads = []
        self.is_running = False
        self.is_dead = False

    def _death(self):
        for thread in self.threads:
            thread.join()
        self.is_running = False
        self.is_dead = True

    def add(self, thread):
        self.threads.append(thread)

    def start(self):
        death_thread = threading.Thread(target=self._death)
        self.is_running = True
        for thread in self.threads:
            thread.start()
        death_thread.start()

