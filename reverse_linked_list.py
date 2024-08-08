class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        #initialize prev to null
        prev = None
        #perform the below operation until the end of the LinkedList
        while(curr):
            #each step move curr to the right, the temp stores this
            tmp = curr.next
            #in the very first step, the curr.next is set to null, this indicates the end of the linked list, in the next steps,
            #we set the curr.next to the previous node in the linked list
            curr.next = prev
            #now make the previous node point to the current node, so in next iteration, the curr.next correctly points to this node
            prev = curr
            #move the current node to the right
            curr = tmp
        return prev

head = ListNode()
curr = head
#create a LinkedList of size 8
for i in range(1,8):
    curr.next = ListNode(i)
    curr = curr.next
sol = Solution()
reverse = sol.reverseList(head)
#print this reversed linked list
while reverse:
    print(reverse.val)
    reverse = reverse.next