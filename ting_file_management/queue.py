class Queue:
    def __init__(self):
        self.info = []

    def __len__(self):
        return len(self.info)

    def enqueue(self, value):
        return self.info.append(value)

    def dequeue(self):
        return self.info.pop(0)

    def search(self, index):
        if(0 <= index < len(self.info)):
            return self.info[index]
        raise IndexError
