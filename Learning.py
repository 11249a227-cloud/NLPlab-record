class Calculator:
    def __init__(self):
        self.current = 0
        self.total = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current
