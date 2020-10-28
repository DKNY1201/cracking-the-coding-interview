"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

To solve this problem without buffer.
Solution1: We can do merge sort. After sorted, all nodes have same values will be nearby so they are easy to be removed
T(n): nlog(n)

Solution2: Have 2 pointers. Normal pointer goes one by one and the other to from that pointer to the tail and compare if
is there any node equal to the value of current pointer and remove it.
T(n): n^2
"""
import unittest
from LinkedList import LinkedList


def remove_dup(ll):
    if not ll.head:
        return

    seen = set()
    prev = head = ll.head

    while head:
        if head.val in seen:
            prev.next = head.next
            head.next = None
            head = prev.next
        else:
            seen.add(head.val)
            prev = head
            head = head.next


class Test(unittest.TestCase):
    def test_remove_dup(self):
        ll = LinkedList()
        vals = [7, 3, 4, 5, 6, 7, 10, 100, 4, 7]
        ll.add_nodes_to_tail(vals)
        remove_dup(ll)
        expect = [7, 3, 4, 5, 6, 10, 100]
        self.assertEqual(expect, ll.to_list(), "Should remove all duplicate nodes from LinkedList")

        ll = LinkedList()
        vals = [-7, -10, -9, 1, 4, 0, 666, 4332, 334, 52, -7, 666, -1, -1, 1]
        ll.add_nodes_to_tail(vals)
        remove_dup(ll)
        expect = [-7, -10, -9, 1, 4, 0, 666, 4332, 334, 52, -1]
        self.assertEqual(expect, ll.to_list(), "Should remove all duplicate nodes from LinkedList")

        ll = LinkedList()
        vals = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        ll.add_nodes_to_tail(vals)
        remove_dup(ll)
        expect = [1]
        self.assertEqual(expect, ll.to_list(), "Should remove all duplicate nodes from LinkedList")

        ll = LinkedList()
        vals = []
        ll.add_nodes_to_tail(vals)
        remove_dup(ll)
        expect = []
        self.assertEqual(expect, ll.to_list(), "Should remove all duplicate nodes from LinkedList")