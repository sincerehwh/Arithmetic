
# 树的结构：
#	
#	节点的度：
#	树的度：
#	叶节点、终端节点：
#	父节点、父亲节点：
#	子节点、孩子节点：
#	兄弟节点：
#	节点的层次：根为第一层
#	树的高度-深度：树中节点的最大层次
#	堂兄节点：
#	节点的祖先：从根到该节点所经分支上的所有节点
#	子孙：以某一节点为根的子树中的任意节点
#	森林：由m(m>=0)棵互不相交的树的集合称为森林
#

#  树的种类：
#	
#	1.无序树：任意点的子节点之间没有顺序关系
#
#	2.有序树：
#		二叉树：
#			完全二叉树：
#			满二叉树：
#			平衡二叉树（AVL）：当且仅当任何节点的两颗子树的高度差不大于1的二叉树（长度差）
#			排序二叉树（Binary Search Tree）：二叉查找树、二叉搜索树、有序二叉树
#
#		霍夫曼树（用于信息编码）：带权最短的二叉树，也称为最优二叉树
#		B树：对读写优化的自平衡的二叉查找树，能够保持数据有序，拥有多余子树
#


# 树的存储和表示：
# 	顺序存储：将数据结构存储在固定的数组中，然在遍历速度上有一定的优势，但因所占空间比较大，是非主流二叉树。二叉树通常以链式存储。
# 	链式存储：由于对节点的个数无法掌握，常见树的存储表示都转换成二叉树进行处理，子节点个数最多为2


# 常见的一些树的应用场景
# 	1.xml，html等，那么编写这些东西的解析器的时候，不可避免用到树
# 	2.路由协议就是使用了树的算法
# 	3.mysql数据库索引
# 	4.文件系统的目录结构
# 	5.所以很多经典的AI算法其实都是树搜索，此外机器学习中的 decision tree 也是树结构


# 二叉树
#	left subtree
#	right subtree
#
# 性质1: 在二叉树的第i层上至多有2^(i-1)个结点（i>0）
# 性质2: 深度为k的二叉树至多有2^k - 1个结点（k>0）
# 性质3: 对于任意一棵二叉树，如果其叶结点数为N0，而度数为2的结点总数为N2，则N0=N2+1;
# 性质4:具有n个结点的完全二叉树的深度必为 log2(n+1)
# 性质5:对完全二叉树，若从上至下、从左至右编号，则编号为i 的结点，其左孩子编号必为2i，其右孩子编号必为2i＋1；
#	   其双亲的编号必为i/2（i＝1 时为根,除外）
#

# 完全二叉树：
#  若设二叉树的高度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，
#  第h层有叶子结点，并且叶子结点都是从左到右依次排布，这就是完全二叉树。
#
# 满二叉树：
#  除了叶结点外每一个结点都有左右子叶且叶子结点都处在最底层的二叉树。
#
# 二叉树遍历
#	  _____a_____
#     |         |    
# 	__b__     __c__    
#   |   |     |   |    
#  _d_ _e_   _f_  _g_                
#  | | | |   | |  | |
#  h i j k   l m  n o
#
#	深度优先遍历(先序、中序、后序)：
#		先序：a,b,d,h,i,e,j,k,c,f,l,m,g,n,o
#		中序：h,d,i,b,j,e,k,a,l,f,m,c,n,g,o
#		后序：h i d j k e b l m f n o g c a
#
# 	广度优先遍历(层次遍历)：
#		

class TreeNode(object):

	def __init__(self,element=0,left_leaf=None,right_leaf=None):
		self.element = element
		self.left_leaf = left_leaf
		self.right_leaf = right_leaf


class Tree(object):

	def __init__(self,root=None):
		self.root = root

	def add(self,element): 
		node = TreeNode(element)
		if self.root == None:
			self.root = node
		else:
			queue = [self.root]
			while queue:
				current = queue.pop(0)
				if current.left_leaf == None:
					current.left_leaf = node
					return
				elif current.right_leaf == None:
					current.right_leaf = node
					return
				else:
					queue.append(current.left_leaf)
					queue.append(current.right_leaf)


	def breadth_traversal(self):
		queue = [self.root]
		while queue:
			current = queue.pop(0)
			print(current.element)
			if current.left_leaf is not None:
				queue.append(current.left_leaf)
			if current.right_leaf is not None:
				queue.append(current.right_leaf)
	
	def pre_deep_travelsal(self,root): # 根，左，右
		if root is None:
			return
		print(root.element,end=" ")
		self.pre_deep_travelsal(root.left_leaf)
		self.pre_deep_travelsal(root.right_leaf)


	def in_deep_travelsal(self,root): # 左，根，右
		if root is None:
			return
		self.in_deep_travelsal(root.left_leaf)
		print(root.element,end=' ')
		self.in_deep_travelsal(root.right_leaf)

	def post_deep_travelsal(self,root): # 左，右，根
		if root is None:
			return
		self.post_deep_travelsal(root.left_leaf)
		self.post_deep_travelsal(root.right_leaf)
		print(root.element,end=',')


tree = Tree()
tree.add('a')
tree.add('b')
tree.add('c')
tree.add('d')
tree.add('e')
tree.add('f')
tree.add('g')
tree.add('h')
tree.add('i')
tree.add('j')
tree.add('k')
tree.add('l')
tree.add('m')
tree.add('n')
tree.add('o')
tree.post_deep_travelsal(tree.root)
		





