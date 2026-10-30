class Solution(object):
    def mergeTwoLists(self, list1, list2):

        listnode = []

        while list1:
            listnode.append(list1.val)
            list1 = list1.next

        while list2:
            listnode.append(list2.val)
            list2 = list2.next

        listnode.sort()

        dummy = ListNode()
        current = dummy

        for x in listnode:
            current.next = ListNode(x)
            current = current.next

        return dummy.next