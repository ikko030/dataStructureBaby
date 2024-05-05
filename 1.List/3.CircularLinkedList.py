from LinkedList import ListNode

class CircularLinkedList:
    def __init__(self):
        self.tail = ListNode("dummy", None)
        self.tail.next = self. tail
        self.__numItems = 0

    def insert(self,i:int, newItem) -> None:
        if (i>=0 and i<= self.__numItems):
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            
            if i == delf.__numItems:
                self.__tail = newNode
            
            self.__numItems += 1
        
        else:
            print("index", i , ":out of bound in insert()")