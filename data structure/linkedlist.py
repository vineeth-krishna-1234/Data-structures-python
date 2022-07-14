
#linked list data structure with its functions like adding values,deleting and displaying

#each node of a linked list 
from os import link


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
            print(displaypointer.data,end=" -> ")
            displaypointer=displaypointer.next
        print("\n")
        


    #append Nodes to the linked list
    def append_nodes(self):
        emptypointer=None
        Noofinputs=int(input('Enter the no of nodes >'))
        for i in range(Noofinputs):
            forInput=input(f"enter node {i} value > ")
            nodepointer=Node(forInput)
            if not self.head:
                self.head=nodepointer
                emptypointer=self.head
            else:
                while emptypointer.next:
                    emptypointer=emptypointer.next
                else:
                    emptypointer.next=nodepointer
        
        print("Created a linked list > ")
        self.display_list()


   #add a node to the beginning of the list
    def append_at_begining(self):
        append_value=input("Enter value to append at begining > ")
        headpointer=self.head
        newnode=Node(append_value)
        self.head=newnode
        newnode.next=headpointer
        print("Appended node at begining >")
        self.display_list()



    #add after a given index 
    def append_at_index(self):
        index_value=int(input("Enter node index > "))
        nodepointer=self.head
        count=1
        prev_pointer=None
        while nodepointer:
            if count==index_value:
                Input_value=input(f"Enter value to append at index {index_value} > ")
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
        print(f"Appended node at index {index_value} >")
        self.display_list()

    #append at the end of the list
    def append_at_end(self):
        pointer=self.head
        while pointer.next:
            pointer=pointer.next
        else:
            input_value=input("Enter value to append at the end >")
            newnode=Node(input_value)
            pointer.next=newnode
        print("Appended node at end >")
        self.display_list()

    #delete at the begining
    def delete_at_begining(self):
        self.head=self.head.next
        print("Deleted node at begining >")
        self.display_list()

    #dele at the end
    def delete_at_end(self):
        prev_pointer=None
        current_pointer=self.head
        while current_pointer:
            if current_pointer.next:
                prev_pointer=current_pointer
                current_pointer=current_pointer.next
            else:
                prev_pointer.next=None
                break
        print("Deleted node at end >")
        self.display_list()

    # delete at a given index of the list
    def delete_at_index(self):
        input_index=int(input("Enter the index to delete > "))
        nodepointer=self.head
        prev_nodepoipnter=None
        count=1
        while nodepointer:
            if count==input_index:
                prev_nodepoipnter.next=nodepointer.next
                break
            else:
                prev_nodepoipnter=nodepointer
                nodepointer=nodepointer.next
                count+=1
        print(f"Deleted node at index {input_index} >")
        self.display_list()

linkedlist_obj=Linked_list()

while True:
    user_input=int(input("<--------linked list----------->\n1. Append Values\n2. Append At Begining\n3. Append At End\n4. Append at index\n5. Delete At Begining\n6. Delete At End\n5. Delete At Index\n6. Display\n7. Exit\nYour Input:> "))
    Decision_list=[linkedlist_obj.append_nodes,linkedlist_obj.append_at_begining,linkedlist_obj.append_at_end,linkedlist_obj.append_at_index,linkedlist_obj.delete_at_begining,linkedlist_obj.delete_at_end,linkedlist_obj.delete_at_index,linkedlist_obj.display_list]
    if user_input==7:
        break
    else:
        Decision_list[user_input-1]()


