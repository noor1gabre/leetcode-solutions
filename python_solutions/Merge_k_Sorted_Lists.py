class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    
    def mergeKLists(self, lists):
        if not lists:
            return None
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]