
# 排序算法
#
# 稳定性：
#   原有相等值的相对次序不变


# Bubble Sort :
#   重复遍历要排序的序列，一次比较两个元素，交换位置，直到不需要交换为止
#
# 运行步骤：1.比较临近两个元素，大数后挪；
#		  2.重复比较后挪的数字与下一位数字，最大数字挪到队尾；
# 		  3.对除最后一个元素的部分重复上述过程；
#		  4.直到无数字可比较。
# 
# 最优时间复杂度：O(n)
# 最差时间复杂度：O(n^2)
#
def bubble_sort(array):
    totalturns = len(array)-1
    for turn in range(0,totalturns):
    	remined_times = totalturns-turn # 内层需要比较的次数
    	change_times = 0 # 交换次数--> 优化
    	for index in range(0,remined_times):
    		if array[index] > array[index+1]:
    			array[index],array[index+1] = array[index+1],array[index]
    			change_times += 1
    	if change_times == 0:
    		return array
    return array


# Select Sort:
#	选出最小的放到最前面，一直到放完为止
#
# 
# 最优时间复杂度：O(n^2)
# 最差时间复杂度：O(n^2)
# 
def select_sort(array):
	n = len(array)
	for turn in range(n-1):
		min_element_index = 0
		for index in range(min_element_index+1,):
			if array[min_element_index] > array[index]:
				min_element_index = index
			array[turn],array[min_element_index] = array[min_element_index],array[turn]
	return array


a = select_sort([2,1,3,11,100,1])
print(a)



