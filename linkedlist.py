class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " --> "
            temp_node = temp_node.next

        return result 
    
    def append(self,value):
        '''add at the end'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self,value):
        ''' add at the end '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node   
        
        self.length += 1

    def insert(self,value,index):
        new_node = Node(value)
        if index <0 or index>self.length:
            return False
        if self.head is None:
            self.head =  new_node
            self.tail = new_node
        
        for _ in range(0,index-1):
            temp_node = self.head.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        return True
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
    def search(self,value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            index+=1
            current_node = current_node.next
        return -1
    def get(self,index):
        current = self.head
        if index <0 or index > self.length :
            return None
        for _ in range(index):
            current = current.next
        return current

    def set_value(self,index,new_value):
        temp = self.get(index)
        if temp:
            temp.value = new_value
            return True
        else:
            return False

    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head   = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0 :
            return None
        if self.length == 1:
            self.head=self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.length-=1
            return popped_node
        
    def removed(self,index):
        if index <0 or index>=self.length:
            return None
        if index == 0 :
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length-=1
            return popped_node.value

    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node
    def k_to_last(self,k):
        # from coding interview
        leader,follower = self.head,self.head
        count = 0
        while leader:
            if count>=k:
                follower=follower.next
            count+=1
            leader=leader.next
        return follower
    def removeNthFromEnd(self,  n: int): #head: Optional[ListNode],
        leader = follower = self.head
        count = 0
        previous = Node(0)
        while leader:
            if count>=n:
                previous = follower
                follower = follower.next
            count+=1
            leader = leader.next
        previous.next = follower.next
        print(follower.value,follower.next)
        # follower.next = None
        print(follower.value,follower.next)
        if follower.next is None:
            print("here")
            
            return Node().value    
        return self.head
new_linked_list = LinkedList()
new_linked_list.append(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# new_linked_list.append(50)
print(new_linked_list.__str__())

new_linked_list.removeNthFromEnd(1)
print(new_linked_list.__str__())
# cracking interview testing

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)

# print(new_linked_list.length)
# print(new_linked_list.__str__())
# new_linked_list.prepend(23)
# print(new_linked_list.__str__())
# print(new_linked_list.length)
# new_linked_list.insert(33,2)
# print(new_linked_list.__str__())
# print(new_linked_list.set_value(0,1134))
# print(new_linked_list.__str__())
# print(new_linked_list.pop_first())
# print(new_linked_list.__str__())
# print(new_linked_list.pop())
# print(new_linked_list.__str__())
# new_linked_list.append(30)
# new_linked_list.append(230)
# new_linked_list.append(140)
# new_linked_list.append(250)
# new_linked_list.append(107)
# new_linked_list.append(2890)
# print(new_linked_list.__str__())
# print(new_linked_list.removed(5))

# print(new_linked_list.__str__())