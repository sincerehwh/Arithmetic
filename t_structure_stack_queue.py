


# 栈结构：Last in first Out
#
# 要求：只允许一端添加数据
#
#
#   ┌─────┐          ┌──────┐             
#   │ Out │◀──┐    ┌─┤  In  │             
#   └─────┘   │    │ └──────┘             
#             │    ▼                      
#           ┌─┴──────┐                    
#  top ───▶ │   n    │ ◀─── top element   
#           ├────────┤                    
#           │   .    │                    
#           ├────────┤                    
#           │   .    │                    
#           ├────────┤                    
#           │   .    │                    
#           ├────────┤                    
#           │   3    │                    
#           ├────────┤                    
#           │   2    │                    
#           ├────────┤                    
# bott ───▶ │   1    │◀─── bottom element 
#           └────────┘                    


# 顺序表实现栈

class Stark(object):


	def __init__(self):
		self.__list = []

	def push(self,item):
		self.__list.append(item)

	def pop(self):
		self.__list.pop()

	def peek(self):
		return self.__list[-1]

	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)


# 队列结构：First in first out
# 
#
#            ┌──────┐
#          ┌─┤  In  │
#          │ └──────┘
#          ▼         
#      ┌────────┐    
#      │   n    │    
#      ├────────┤    
#      │   .    │    
#      ├────────┤    
#      │   .    │    
#      ├────────┤    
#      │   .    │    
#      ├────────┤    
#      │   3    │    
#      ├────────┤    
#      │   2    │    
#      ├────────┤    
#      │   1    │    
#      └───┬────┘    
# ┌─────┐  │         
# │ Out │◀─┘         
# └─────┘            

class Queue(object):


	def __init__(self):
		self.items = []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		self.items.pop(0)

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)


class Double_queque(object):

    """双端队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def add_front(self, item):
        """在队头添加元素"""
        self.items.insert(0,item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.items.append(item)

    def remove_front(self):
        """从队头删除元素"""
        return self.items.pop(0)

    def remove_rear(self):
        """从队尾删除元素"""
        return self.items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.items)


