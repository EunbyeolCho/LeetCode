"""
팰린드롬 연결 리스트
연결 리스트가 팰린드롬 구조인지 판별하라.
"""
import collections

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class isPalindrome(object):

    def method1(self, head:ListNode) -> bool: #리스트 변환
        q : List = []
        
        if not head:
            return True
        node = head

        #Convert to list
        while node is not None:
            q.append(node.val)
            node = node.next

        #Determine if palindrome
        while len(q) > 1:
            if q.pop(0) != q.pop(): #비효율적 : 동적배열로 구성된 리스트는 맨 앞 아이템 가져오면 모든 값이 한칸씩 시프팅
                return False
        return True



    def method2(self, head:ListNode) -> bool: #데크

        #Define deque datatype
        q : Deque = collections.deque()
        
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        #Determine if palindrome
        while len(q)>1:
            if q.popleft() != q.pop(): #데크는 이중연결리스트 구조로 효율적
                return False
        return True

    def method3(self, head:ListNode) -> bool: #런너 기법, BEST ANSWER!
        rev = None
        slow = fast = head

        #Configure Reverse Link List with Runner
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast: #입력값이 홀수일 때 slow는 한칸 더 가야함
            slow = slow.next
        
        #Determine if palindrome
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev



if __name__ == '__main__':

    head = ListNode(1,ListNode(2, ListNode(2, ListNode(1, None)))) 
    print(isPalindrome().method1(head))
    print(isPalindrome().method2(head))
    print(isPalindrome().method3(head)) #best method : 연결리스트를 변환하지 않고 풀이
