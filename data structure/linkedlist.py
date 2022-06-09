
#linked list data structure with its functions like adding values,deleting and displaying


class Node:
    def __init__(self,data):
        self.data = data
        self.next=None


class Linked_list:


    def __init__(self):
        self.head=None


    #display the linked list
    def display_list(self):
        displaypointer=self.head
        while displaypointer:
            print(displaypointer.data)
            displaypointer=displaypointer.next


    #append Nodes to the linked list
    def append_nodes(self):
        emptypointer=None
        for i in range(6):
            forInput=int(input("enter node"))
            nodepointer=Node(forInput)
            if not self.head:
                self.head=nodepointer
                emptypointer=self.head
            else:
                while emptypointer.next:
                    emptypointer=emptypointer.next
                else:
                    emptypointer.next=nodepointer


   #add a node to the beginning of the list
    def append_at_begining(self):
        append_value=int(input("enter append value"))
        headpointer=self.head
        newnode=Node(append_value)
        self.head=newnode
        newnode.next=headpointer


    #add after a given index 
    def append_at_index(self):
        index_value=int(input("enter node index"))
        nodepointer=self.head
        count=0
        prev_pointer=None
        while nodepointer:
            if count==index_value:
                Input_value=int(input("enter value at index"))
                newnode=Node(Input_value)
                nextpointer=nodepointer.next
                prev_pointer.next=newnode
                newnode.next=nextpointer
                break
            elif count+1==index_value:
                count+=1
                prev_pointer=nodepointer
            else:
                count+=1
                nodepointer=nodepointer.next


    def append_at_end(self):
        pointer=self.head
        while pointer.next:
            pointer=pointer.next
        else:
            input_value=int(input("enter end append value"))
            newnode=Node(input_value)
            pointer.next=newnode


    def delete_at_begining(self):
        self.head=self.head.next


    def delete_at_end(self):
        prev_pointer=None
        current_pointer=self.head
        while current_pointer:
            print("hello")
            if current_pointer.next:
                prev_pointer=current_pointer
                current_pointer=current_pointer.next
            else:
                prev_pointer.next=None
                break
    def delete_at_index(self):
        input_index=int(input("enter the index to delete"))
        nodepointer=self.head
        prev_nodepoipnter=None
        count=0
        while nodepointer:
            if count==input_index:
                prev_nodepoipnter.next=nodepointer.next
                break
            else:
                prev_nodepoipnter=nodepointer
                nodepointer=nodepointer.next
                count+=1


while True:
    input("MENU\n1. Enter the values of the linked list\n2.Append a node at begining\n3.append at a particular index\n4.append at the end\n 5.delete_at_index")


linkedlist1=Linked_list()
linkedlist1.append_nodes()
linkedlist1.append_at_begining()
linkedlist1.append_at_index()
linkedlist1.append_at_end()
linkedlist1.delete_at_index()
linkedlist1.display_list()


