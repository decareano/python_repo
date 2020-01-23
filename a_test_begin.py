class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self): 
        #self.head = None
        self.begin = None
        self.end = None
        self.num_nodes = 0
        
    def push(self, new_data): 
        # new_node = ListNode(new_data) 
        # new_node.next = self.head 
        # self.head = new_node 
        if self.begin is None:
            self.begin = ListNode(new_data)
        elif self.end is None:
            self.end = ListNode(new_data)
            self.begin.next = self.end
        else:
            new_node = ListNode(new_data)
            self.end.next = new_node
            self.end = new_node
        self.num_nodes += 1

l1 = LinkedList()
l2 = LinkedList()

l1.push(6)
l1.push(4)
l1.push(9)

