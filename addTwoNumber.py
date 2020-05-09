'''
#You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''


class Solution:
    def addTwoNumbers(self, l1, l2,ListNode):

        # first create a cuurent and resultlist

        resultlist = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            # or - because if number of elements are diff. in any of the list

            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)

            current = current.next

            carry = carry // 10

        return resultlist.next
