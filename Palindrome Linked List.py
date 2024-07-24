# using list 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        current=head
        while current:
            vals.append(current.val)
            current=current.next
        return vals== vals[::-1]


# slightly complex one
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    if not head:
        return True

    # Find the end of the first half and reverse the second half
    def end_of_first_half(node):
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(node):
        prev = None
        curr = node
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    first_half_end = end_of_first_half(head)
    second_half_start = reverse_list(first_half_end.next)

    # Check whether there is a palindrome
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next

    # Restore the list and return the result
    first_half_end.next = reverse_list(second_half_start)
    return result
