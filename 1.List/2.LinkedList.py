class ListNode:
    def __init__(self, newItem, nextNode: 'ListNode'):
        self.item = newItem
        self.next = nextNode


class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    # 원소 삽입
    def insert(self, i: int, newItem):              # dummy => 10 => 12// newItem = 11
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)            #prev = 10
            newNode = ListNode(newItem, prev.next)  # newNode(newItem, prev.next =>12)
            prev.next = newNode                     # prev.next => newNode

            self.__numItems += 1

        else:
            print("index", i, "out of bound in insert()")

    # i번 노드 알려주기
    def __getNode(self, i: int) -> ListNode:
        curr = self.__head  # 더미 헤드는 index = -1
        for index in range(i + 1):
            curr = curr.next
        return curr

    # 원소 추가하기
    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(newItem, prev.next)  # newNode(newItem, prev.next => None)
        prev.next = newNode  # prev.next => newNode

        self.__numItems += 1

    # 원소 삭제하기
    def pop(self, i: int):
        if (i >= 0 and i <= self.__numItems - 1):
            prev = self.__getNode(i - 1)
            curr = prev.next
            prev.next = curr.next
            reItem = curr.item

            self.__numItems -= 1
            return reItem
        else:
            return None

        # 원소 x 제거하기(x가 여럿 있으면 앞의 노트를 삭제)

    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next

        self.__numItems -= 1

    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__head  # prev = 더미헤드
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next  # 다음 노드로 이동

        return (None, None)

    # 기타 작업

    # i번 원소 리턴
    def get(self, i: int):
        if self.isEmpty():
            return newNode

        if (i >= 0 and i <= self.__numItems - 1):
            return self.__getNode(i).item
        else:
            return None

    # x가 몇 번 원소인지 알려주기
    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -12345

    # 기타의 기타
    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0

    # x가 몇 개 있는지 세기
    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt

    # 굉장히 비효율적인 함수 in 연결리스트
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))

    def copy(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a

    def reverse(self):
        a = LinkedListBasic()  # a는 그저 tmp같은 존재 ㅠ
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()  # why? => 역순으로 다시 넣을려고
        for index in range(a.size()):
            self.append(a.get(index))

    def sort(self) -> None:
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear
        for index in range(len(a)):
            self.append(a.get[index])

    # 연결 리스트 프린트!
    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end=' ')
            curr = curr.next
        print()


# 테스트
list = LinkedListBasic()
list.append(30);
list.insert(0, 20)

a = LinkedListBasic()
a.append(4);
a.append(3);
a.append(3);
a.append(2);
a.append(1)
list.extend(a)
list.reverse()
list.pop(0)

print("count(3): ", list.count(3))
print("get(2): ", list.get(2))
list.printList()