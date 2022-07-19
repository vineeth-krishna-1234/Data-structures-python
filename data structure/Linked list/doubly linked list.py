

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Doubly_linked_list:
    def __init__(self):
        self.head=None

    def Display(self):
        Display_pointer=self.head
        while Display_pointer:
            print(Display_pointer.data)
            Display_pointer=Display_pointer.next

    def Include_Data(self):
        prevpointer=None
        empty_pointer=None
        for i in range(5):
            Newnode=Node(input("Enter Node value"))
            if not self.head:
                self.head=Newnode
                empty_pointer=self.head
            else:
                empty_pointer.next=Newnode
                prevpointer=empty_pointer
                empty_pointer=empty_pointer.next
                empty_pointer.prev=prevpointer


    def Include_At_begining(self):
        empty_pointer=None
        Newnode=Node(input("Enter Node value to include at begining:"))
        if self.head:
            empty_pointer=self.head
            self.head.prev=Newnode
            self.head=Newnode
            self.head.next=empty_pointer
        else:
            self.head=Newnode
    def Include_At_index(self):
        next_pointer=None
        index_value=int(input("Enter index value"))
        traverse_pointer=self.head
        traverse_index=0
        while traverse_pointer:
            if traverse_index-1==index_value:
                Newnode=Node(input("Enter value to inclue at the index"))
                next_pointer=traverse_pointer.next
                traverse_pointer.next=Newnode
                Newnode.next=next_pointer
            traverse_index+=1
            traverse_pointer=traverse_pointer.next

        
    
    


       

do=Doubly_linked_list()
do.Include_Data()
do.Include_At_begining()
do.Include_At_index()
do.Display()