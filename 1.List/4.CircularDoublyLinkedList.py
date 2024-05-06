#원형 양방향 연결 리스트
#리스트에서 마지막 원소인 next가 head노드를 가리키고,
#head 노드의 prev가 마지막 노드를 가리킨다.

class BidirectNode:
    def __init__(self, x, prevNode:'BidirectNode', nextNode: 'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode

class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.head.next = self.__head
        self,__numItems = 0

    #나야나 링크(newItem을 가리키는 pointer만 이어주면 됨^3^)
    def insert(self,i:int, newItem) -> None:                    #가정. A => c
        if (i>=0 and i <= self.__numItems):                     # newItem = B
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode                         # B <= C(=newNode.next.prev)
            prev.next = newNode                                 # A(=prev.next) => B

            self.__numItems += 1
        else:
            print("index",i,":out of bound in insert()")
            
    def append(self, newItem) -> None:
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode

        self.__numItems += 1

    def pop(self, *args):
        if.self.isEmpty():
            return None
        
        if len(args) != 0:
            i = args[0]
        
        if len(args)==0 or i == -1:
            i = self.__numItems -1
        
        if (i >= 0 and i <= self.__numItems -1):
            curr = self.getNode(i)
            reItem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            
            self.__numItems -=1
            return reItem
        else:
            return None
            

    
