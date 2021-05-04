"""
2020.05.04
두 정렬 리스트의 병합
정렬되어 있는 두 연결 리스트를 합쳐라.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class mergeTwoLists(object):

    def method1(self, l1:ListNode, l2:ListNode) -> ListNode:

        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1 : #l1이 None이 되면 재귀가 끝나고 리턴
            l1.next = self.method1(l1.next, l2)
        return l1
 

if __name__ == '__main__':

    list1 = ListNode(1,ListNode(2, ListNode(4, None)))
    list2 = ListNode(1,ListNode(3, ListNode(4, None)))

    result_list = mergeTwoLists().method1(list1,list2)
    
    while result_list.next:

        print(result_list.val, end=' ')
        result_list = result_list.next
