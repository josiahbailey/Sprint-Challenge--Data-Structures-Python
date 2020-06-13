class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, curr, prev):
        if curr is None:
            return
        if curr.next_node is None:
            self.head = curr
            curr.next_node = prev
            return

        next_node = curr.next_node
        curr.next_node = prev
        self.reverse_list(next_node, curr)

    # def reverse_list(self, node, prev):
    #     if node is None:
    #         return node

    #     if node.next_node is None:
    #         return node

    #     new_node = self.reverse_list(node.next_node, None)

    #     node.next_node.next_node = node

    #     node.next_node = None

    #     self.head = node
        # if (node == None):
        #     return node
        # if (node.next_node == None):
        #     return node

        # new_node = self.reverse_list(node.next_node, None)
        # node.next_node.next_node = node
        # node.next_node = None
        # self.head = new_node
        # prev = prev
        # current = node
        # if current.next_node:
        #     next_node = current.next_node
        #     current.next_node = prev
        #     prev = current
        #     current = next_node
        # self.reverse_list(current, prev)
        # self.head = prev

        # first = node
        # current = node
        # next_node = current.next_node
        # current.next_node = prev
        # prev = current
        # current = next_node
