#optimized one
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow ==fast:
                break
        else:
            return None

        # find start of cycle
        slow=head
        while slow!=fast:
            slow= slow.next
            fast= fast.next
        return slow
            


# brute force
def detectCycle(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return current
        visited.add(current)
        current = current.next
    return None
