from platform import node
from time import sleep
from pkg_resources import empty_provider


class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Doubly_linked_list:
    def __init__(self):
        self.head=None
    def Include_Data(self):
        prevpointer=None
        empty_pointer=None
        next_pointer=None
        for i in range(5):
            Newnode=Node(input("Enter Node value"))
            if not self.head:
                self.head=Newnode
                empty_pointer=self.head
                prevpointer=self.head
            else:
                empty_pointer.next=Newnode
                prevpointer=empty_pointer
                empty_pointer=empty_pointer.next
                empty_pointer.prev=prevpointer
    def Display(self):
        Display_pointer=self.head
        while Display_pointer:
            print(Display_pointer.data)
            Display_pointer=Display_pointer.next


       

do=Doubly_linked_list()
do.Include_Data()
do.Display()