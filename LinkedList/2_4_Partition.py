"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
import unittest
from LinkedList import LinkedList


def partition(ll, x):
    if not ll or not ll.head:
        return ll.head

    less = dummy_less = greater = dummy_greater = None
    head = ll.head

    while head:
        if head.val < x:
            if not less:
                less = head
                dummy_less = head
            else:
                less.next = head
                less = head
        else:
            if not greater:
                greater = head
                dummy_greater = head
            else:
                greater.next = head
                greater = head

        head = head.next

    if less:
        less.next = dummy_greater

    if greater:
        greater.next = None

    ll.head = dummy_less if dummy_less else dummy_greater


class Test(unittest.TestCase):
    def test_partition(self):
        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        expect = [3, 4, 5, 6, 4, 7, 7, 10, 100, 7]
        partition(ll, 7)
        self.assertEqual(expect, ll.to_list(), "Should partition linkedlist nodes around given x")

        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        expect = [7, 3, 4, 5, 6, 7, 4, 7, 10, 100]
        partition(ll, 8)
        self.assertEqual(expect, ll.to_list(), "Should partition linkedlist nodes around given x")

        ll = LinkedList()
        vals = [-7, -3, -4, 5, 6, 7, 10, 100, -4, 7]
        ll.add_nodes_to_tail(vals)
        expect = [-7, -3, -4, -4, 5, 6, 7, 10, 100, 7]
        partition(ll, 0)
        self.assertEqual(expect, ll.to_list(), "Should partition linkedlist nodes around given x")

        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        expect = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        partition(ll, 2)
        self.assertEqual(expect, ll.to_list(), "Should partition linkedlist nodes around given x")

        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7, 100]
        ll.add_nodes_to_tail(vals)
        expect = [7, 3, 4, 5, 6, 7, 10, 4, 7, 100, 100]
        partition(ll, 100)
        self.assertEqual(expect, ll.to_list(), "Should partition linkedlist nodes around given x")