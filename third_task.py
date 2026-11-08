class min_stack:
    def __init__(self):
        self.stack = []

    def top(self) -> int:
        return self.stack[-1][1]

    def get_min(self) -> int:
        return self.stack[-1][0]

    def push(self, arg) -> None:
        if len(self.stack) != 0:
            self.stack.append([min(self.get_min(), arg), arg])
        else:
            self.stack.append([arg, arg])

    def pop(self) -> None:
        self.stack.pop()
