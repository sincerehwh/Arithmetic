

# 搜索：
#
#	1.二分查找法 
#	2.顺序查找
#	3.二叉树查找
#	4.哈希查找
#


# 二分查找法：
#
#	最优时间复杂度：O(1)
#	最坏时间复杂度：O(logn)
#	优点：是比较次数少，查找速度快，平均性能好
#	缺点：是要求待查表为有序表，且插入删除困难

def binary_search_1(array,item):
	first = 0
	last = len(array)-1
	while first<=last:
		middlepointer = (first+last) // 2
		if array[middlepointer] == item:
			return True
		elif item < array[middlepointer]:
			last = middlepointer-1
		else:
			first = middlepointer+1
		return False

	return False


def binary_search_2(array, item):
	if len(array) == 0:
		return False
	else:
		middlepointer = len(array)//2
		if array[middlepointer]==item:
			return True
		else:
			if item < array[middlepointer]:
				return binary_search_2(array[:middlepointer],item)
			else:
				return binary_search_2(array[middlepointer+1:],item)


