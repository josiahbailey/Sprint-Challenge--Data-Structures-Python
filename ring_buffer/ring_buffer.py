class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.counter = 0

    def append(self, item):
        # item can always be added
        # if capcity is full then the last item is deleted
        # items must stay in the order they are added
        if len(self.storage) is self.capacity:
            self.storage[self.counter] = item
            self.counter += 1
            if self.counter == self.capacity:
                self.counter = 0
        else:
            self.storage.append(item)

    def get(self):
        return self.storage
