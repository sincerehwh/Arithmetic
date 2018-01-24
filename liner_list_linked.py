

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


if __name__ == "__main__":
	dll = DoubleDirectionLinkList()
	dll.insert(0,1000)
	dll.add(999)
	# dll.remove()
	dll.travel()





