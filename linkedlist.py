from node import Node


class TuplesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, key, value):
        node_tuple = (key, value)
        n = Node(node_tuple)
        if self.first is None:
            self.first = n
            self.last = n
        else:
            self.last.link(n)
            self.last = n

    def get(self, index):
        counter = 0
        current_node = self.first
        while current_node is not None:
            if counter == index:
                return current_node
            else:
                current_node = current_node.next
                counter += 1
        return None

    def find(self, search_input):
        current_node = self.first
        while current_node is not None:
            if current_node.value[0] == search_input:
                return current_node.value
            else:
                current_node = current_node.next
        return None
