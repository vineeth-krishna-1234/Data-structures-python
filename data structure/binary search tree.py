from hashlib import new
from logging import root
from operator import ne


class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Binary_tree:
    def __init__(self):
        self.root=None
    

    #adding multiple values
    def add_values(self):
        nodepointer=None
        for i in range(1,10):
            userinput=int(input("Enter node value:"))
            newnode=Node(userinput)
            if not self.root:
                self.root=newnode
                nodepointer=self.root
            else:
                while True:
                    if userinput>nodepointer.data:
                        if not nodepointer.right:
                            nodepointer.right=newnode
                            nodepointer=self.root
                            break
                        else:
                            nodepointer=nodepointer.right
                    else:
                        if not nodepointer.left:
                            nodepointer.left=newnode
                            nodepointer=self.root
                            break
                        else:
                            nodepointer=nodepointer.left
    def Display_values(self):
        ptr=self.root
        while ptr:
            print(ptr.data)
            ptr=ptr.right
bt=Binary_tree()
bt.add_values()
bt.Display_values()

