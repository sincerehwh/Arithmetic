

# 单链表：
#			
#  ┌───┐                                                                           
#  │ p ├┐                                                                          
#  └───┘│                                                                          
#       │ ┌─────┬──────┐     ┌──────┬──────┐    ┌──────┬──────┐     ┌──────┬──────┐
#       └▶│ elem│ next ├────▶│ elem │ next │... │ elem │ next ├────▶│ elem │ blank│
#         └─────┴──────┘     └──────┴──────┘    └──────┴──────┘     └──────┴──────┘
# 

# 单向链表节点
class SingleDirectionNode(object):

	def __init__(self,element,):
		self.element = element
		self.next = None

# 单向链表
class SingleDirectionLinkList(object):


	def __init__(self,node=None):
		self.__head = node

	def is_empty(self):
		return self.__head is None

	def length(self):
		current = self.__head # 游标
		length = 0 			  # 数据数量
		while current != None:
			length += 1
			current = current.next
		return length 

	def travel(self):
		current = self.__head
		while  current != None:
			print(current.element,end = " ")
			current = current.next

	def add(self,item):
		node = SingleDirectionNode(item)
		node.next = self.__head
		self.__head = node

	def append(self,item):
		node = SingleDirectionNode(item)
		if self.is_empty():
			self.__head = node
		else:
			current = self.__head
			while current.next != None:
				current = current.next
			current.next = node

	def insert(self,position,item):
		if position <= 0 :
			self.add(item)
		elif position >= (self.length()-1):
			self.append(item)
		else:
			node = SingleDirectionNode(item)	
			current = self.__head
			count = 0
			while count < (position-1):
				count += 1
				current = current.next
			# 循环退出，current指向pos-1
			node.next = current.next
			current.next = node


	def remove(self,item):
		current = self.__head
		pre = None
		while current != None:
			if current.element is item:
				if current == self.__head:
					self.__head = current.next
				else:
					pre.next = current.next
				break
			else:
				pre = current
				current = current.next


	def search(self,item):
		current = self.__head

		while current==None :
			if current.element == item:
				return True
			else:
				cur= cur.next
		return False


# 双向链表：
# 	┌───┐    ┌───┬────────┬───┬───▶┌───┬────────┬───┬───▶┌───┬────────┬───┐
# 	│ p ├───▶│nil│ element│ n │    │ p │ element│ n │    │ p │ element│nil│
# 	└───┘    └───┴────────┴───┘◀───┴───┴────────┴───┘◀───┴───┴────────┴───┘
#

# 双向链表节点
class DoubleDirectionNode(object):


	def __init__(self,item):
		self.element = item
		self.next = None
		self.prev = None

# 双向链表
class DoubleDirectionLinkList(object):


	def __init__(self,node=None):
		self.__head = node

	def is_empty(self):
		return self.__head is None

	def length(self):
		current = self.__head # 游标
		length = 0 			  # 数据数量
		while current != None:
			length += 1
			current = current.next
		return length 

	def travel(self):
		current = self.__head
		while  current != None:
			print(current.element,end = " ")
			current = current.next

	def add(self,item):
		node = DoubleDirectionNode(item)
		if self.is_empty():
			self.__head = node
		else:
			node.next = self.__head
			self.__head.prev = node
			self.__head = node

	def append(self,item):
		node = DoubleDirectionNode(item)
		if self.is_empty():
			self.__head = node
		else:
			current = self.__head
			while current.next != None:
				current = current.next
			current.next = node
			node.prev = current

	def insert(self,position,item):
		if position <= 0:
			self.add(item)
		elif position > (self.length()-1):
			self.append(item)
		else:
			node = DoubleDirectionNode(item)
			current = self.__head
			count = 0
			while  count < (position-1):
				count += 1
				current = current.next
			node.prev = current
			node.next = current.next
			current.next.prev = node
			current.next = node


	def remove(self,item):
		pass
		# if self.is_empty():
		# 	return
		# else:
		# 	current = self.__head
		# 	if current.element == item:
		# 		if current.next == None:
		# 			self.__head = None
		# 		else:
		# 			current.next.prev = None
		# 			self.__head = current.next
		# 		return
		# 	while current != None:
		# 		if current.element == item:
		# 			current.prev.next = current.next
		# 			current.next.prev = current.prev
		# 			break
		# 		current = current.next

	def search(self,item):
		current = self.__head
		while  current != None:
			if current.item == item:
				return True
			current = current.next
		return False


# 单向循环链表
# ┌───┐           │───────────────────────────────────────────────────────────    
# │ p ├┐          │                                                          │    
# └───┘│          ▼                                                          │    
#      │ ┌─────┬──────┐     ┌──────┬──────┐    ┌──────┬──────┐     ┌──────┬──┴───┐
#      └▶│ elem│ next ├────▶│ elem │ next │... │ elem │ next ├────▶│ elem │ head │
#        └─────┴──────┘     └──────┴──────┘    └──────┴──────┘     └──────┴──────┘


class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedlist(object):
    """单向循环链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)
        print("")


    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            #添加的节点指向_head
            node.next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            #_head指向添加node的
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 移到链表尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self._head

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:
                # 尾部删除
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()





