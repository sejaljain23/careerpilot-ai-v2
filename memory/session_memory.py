class SessionMemory:

    def __init__(self):
        self.data = {}
        self.history = []

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def add_history(self, message):
        self.history.append(message)

    def get_history(self):
        return self.history

    def clear(self):
        self.data.clear()
        self.history.clear()