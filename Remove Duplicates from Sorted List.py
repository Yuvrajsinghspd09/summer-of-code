def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return head
    
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head
