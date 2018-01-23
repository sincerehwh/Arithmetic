
# 单向链表
class SingleDirectionNode(object):

	def __init__(self,element,):
		self.element = element
		self.next = None


class SingleDirectionLinkList(object):


	def __init__(self,node=None):
		self.__head = node

	def is_empty(self):
		return self.__head==None

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
		node = SingleDirectionNode(item)
		current = self.__head
		index = 0
		while index==position-1:
			node.next = current
			current = node


	def remove(self,position,item):
		pass

	def search(self):
		pass

if __name__ == "__main__":
	ll = SingleDirectionLinkList()
	print(ll.is_empty())
	ll.add(100)
	ll.add(100)
	ll.add(100)
	ll.insert(1,2)
	ll.travel()



# is_empty() 判断链表是否为空
# length() 返回链表的长度
# travel() 遍历
# add(item) 在头部添加一个节点
# append(item) 在尾部添加一个节点
# insert(pos, item) 在指定位置pos添加节点
# remove(item) 删除一个节点
# search(item) 查找节点是否存在


# 单向循环列表

# 双向链表

