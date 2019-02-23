# coding:utf-8
class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):

    def __init__(self, node=None):

        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):

        # 从1开始就需要判断一下是否为空链表
        if self.is_empty():
            return 0

        cur = self.__head
        count = 1  # count必须从1开始

        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def traval(self):
        cur = self.__head

        if self.is_empty():
            return

        while cur.next != self.__head:
            print(cur.elem)
            cur = cur.next

        print(cur.elem)
        print('')

    def add(self, item):
        node = Node(item)

        # 如果是空列表
        if self.__head == None:
            self.__head = node
            node.next = node
        else:
            # 不是空链表
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next

            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):

        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next

            # node.next = cur.next
            node.next = self.__head
            cur.next = node

    def search(self, item):

        cur = self.__head

        if self.is_empty():
            return False

        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next

        # 最后一个没有判断，所以单独判断
        if cur.elem == item:
            return True
        return False

    def remove(self, item):

        cur = self.__head
        pre = None

        # 如果链表为空链表
        if self.is_empty():
            return

        # 这里指的是非只有一个的情况
        while cur.next != self.__head:
            if cur.elem == item:

                if cur == self.__head:
                    # 头结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next

                    rear.next = self.__head.next
                    self.__head = cur.next

                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

        # 跳出循环之后，cur指向了最后一个元素
        if cur.elem == item:

            # 这里是为了有且只有一个的情况
            if cur == self.__head:
                self.__head = None
            # 删除最后一个
            else:
                pre.next = cur.next


if __name__ == '__main__':
    single = SingleCycleLinkList()

    single.append(8)
    print('length')
    print(single.length())
    print('traval')
    single.traval()
    single.remove(8)
    print('删除928')
    single.traval()















