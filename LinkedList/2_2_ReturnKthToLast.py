"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
import unittest
from LinkedList import LinkedList


def get_kth_to_last_node(ll, k):
    if not ll or not ll.head or k < 1:
        return None

    pioneer = follower = ll.head
    i = 0

    while pioneer and i < k:
        pioneer = pioneer.next
        i += 1

    # k greater than number of nodes
    if i < k:
        return None

    while pioneer:
        pioneer = pioneer.next
        follower = follower.next

    return follower


class Test(unittest.TestCase):
    def test_get_kth_to_last_node(self):
        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        self.assertEqual(100, get_kth_to_last_node(ll, 3).val, "Should return correct kth to last node")

        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        self.assertEqual(7, get_kth_to_last_node(ll, 10).val, "Should return correct kth to last node")

        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        self.assertEqual(None, get_kth_to_last_node(ll, 11), "Should return None if kth node exceeds number of nodes")

        ll = LinkedList()
        vals = []
        ll.add_nodes_to_tail(vals)
        self.assertEqual(None, get_kth_to_last_node(ll, 1), "Should return None if kth node exceeds number of nodes")
