"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next=self.head
        self.head=new_element
        # pass

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        deleted=self.head
        if self.head:
            self.head=self.head.next
            deleted.next=None
        return deleted
        # pass

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        # pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        # pass







# class Stack:
#     def __init__(self):
#         self.stack=list()
#     def push(self, element):
#         self.stack.append(element)
#     def pop(self):
#         if len(self.stack)>0:
#             return self.stack.pop()
#         else:
#             return "No elements"
#     def peek(self):
#         if len(self.stack)>0:
#             return self.stack[len(self.stack)-1]
#         else:
#             return None
    


#         # pass

# obj=Stack()
# obj.push(2)
# print(obj.stack)
# obj.push(1)
# print(obj.stack)
# obj.pop()
# print(obj.stack)