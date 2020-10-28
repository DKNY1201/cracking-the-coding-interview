"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""
import unittest
from LinkedList import LinkedList


def delete_middle_node(ll, middle_node):
    if not ll or not ll.head or not middle_node:
        return

    next = middle_node.next
    middle_node.val = next.val
    middle_node.next = next.next
    next.next = None


class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        expect = [7, 3, 4, 6, 7, 10, 100, 4, 7]
        delete_middle_node(ll, ll.get_k_th_node(3))
        self.assertEqual(expect, ll.to_list(), "Should remove provided middle node")

        ll = LinkedList()
        vals = [7, 3, 4]
        ll.add_nodes_to_tail(vals)
        expect = [7, 4]
        delete_middle_node(ll, ll.get_k_th_node(1))
        self.assertEqual(expect, ll.to_list(), "Should remove provided middle node")