class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_to_tail(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_nodes_to_tail(self, vals):
        for val in vals:
            self.add_node_to_tail(val)

    # Get k th node, zero index
    def get_k_th_node(self, k):
        i = 0
        node = self.head

        while node and i < k:
            i += 1
            node = node.next

        return node if i == k else None

    def to_list(self):
        res = []

        while self.head:
            res.append(self.head.val)
            self.head = self.head.next

        return res


class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None