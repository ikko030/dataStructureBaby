#양방향 연결 리스트
#1. __head가 없어지고 __tail이 생겼다.
#2. 순화를 사용하여 append(), extend(), copy()의 효율성이 대폭 개선되었다!!!
#from LinkedList import ListNode
class ListNode:
    def __init__(self, newItem, nextNode: 'ListNode'):
        self.item = newItem
        self.next = nextNode


class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0



    def insert(self,i:int, newItem) -> None:
        if (i>=0 and i<= self.__numItems):
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            
            if i == self.__numItems:
                self.__tail = newNode                   #마지막에 삽입한 경우, newNode에 tail레퍼런스를 둔다
            
            self.__numItems += 1
        
        else:
            print("index", i , ":out of bound in insert()")


    def append(self, newItem) -> None:
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode                        
        self.__tail = newNode

        self.__numItems += 1



    def pop(self,*args):

        if self.isEmpty():
            return None
        #파라미터 값이 있으면
        if len(args) != 0:
            i = args[0]                         #args는 튜플로 받기 때문에, args[0] 가능
        
        #파라미터 값이 없거나 -1일 때
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        
        
        if ( i >= 0 and i <= self.__numItems -1):
            prev = self.getNode(i-1)
            reItem = prev.next.item
            prev.next = prev.next.next          #없어진 노드 앞의 노드를 prev.next로 바꾼다

            if i == self.__numItems -1:
                self.__tail = prev              #없어진 노드가 마지막 노드였으면, 이전 노드를 tail 레퍼런스 둔다.
            
            self.__numItems -=1
            return reItem

        else:
            return None


    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next =curr.next

            if curr == self.__tail:
                self.__tail = prev
            
            self.__numItems -= 1
            return x
        
        else:
            return None

    def get(self, *args):
        if self.isEmpty():
            return None
        
        if len(args) != 0:
            i = args[0]

        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        
        if (i>= 0 and i <= self.__numItems -1):
            return self.getNode(i).item
        
        else:
            return None

    def index(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        
        return -12345
    
    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__tail == ListNode("dummy", None)
        self.__tail.next = self.__tail

        self.__numItems = 0

    def count(self, x)  -> int:
        cnt = 0
        for element in self:
            if element == x:
                cnt +=1
        
        return cnt

    def extend(self, a):
        for x in a:
            self.append(x)

    def copy(self) -> 'CircularLinkedList':
        a = CircularLinkedList()
        for element in self:
            a.append(element)
        return a

    #한 번 훑으면서 링크를 거꾸로 바꾸는 방식
    def reverse(self) -> None:
        __head = self.__tail.next                                   #__head 는 dummy임
        prev = __head;  curr = prev.next;   next = curr.next        #prev = dummy,   curr = [0], next = [1]
        curr.next = __head; __head.next = self.__tail;  self.__tail = curr      #curr자리에 tail 레퍼런스를 둠
        #위의 코드는 [-1]<-[0]; [-1]->[__tail]; [0]을 tail로 둠
        for i in range(self.__numItems -1):
            prev = curr;    curr = next;    next= next.next
            curr.next = prev                                        #[0]<- [1]

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear
        for element in a:
            self.append(element)

    
    def __findNode(self, x) ->(ListNode, ListNode):
        __head = prev = self.__tail.next    #dummy head
        curr = prev.next                    #[0]번 노드
        while curr != __head:              
             #^^ ?!!! curr이 __head일리 없잖아!!!!?....! => 마지막 노드에서 tail이 레퍼런스 하니까 끝까지 가면 curr = __head가 됨

            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next
            
        return (None, None)

    def getNode(self, i:int) ->ListNode:
        curr = self.__tail.next     #dummy head
        for index in range(i+1):
            curr = curr.next
        return curr

    def printList(self) -> None:
        for element in self:
            print(element, end = ' ')
        print()

    def __iter__(self):
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
        def __init__(self, alist):
            self.__head = alist.getNode(-1)         #dummy head
            self.iterPosition = self.__head.next    #[0]번 노드
        
        def __next__(self):
            if self.iterPosition == self.__head:    #순환 끝!
                raise StopIteration                 #raise가 뭐지?  => 예외 발생시
            
            else:
                item = self.iterPosition.item
                self.iterPosition = self.iterPosition.next
                return item



list = CircularLinkedList()
list.append(30);    list.insert(0, 20)
a = [4,3,3,2,1]
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):",list.get(2))
list.printList()