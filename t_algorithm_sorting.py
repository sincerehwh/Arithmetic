#coding: utf-8 
#!/usr/bin/python   
import random
import time

def get_random_array(max=100,length=1000):
	array = []
	for _ in range(length):
		array.append(random.randint(0,max))
	return array

random_array = get_random_array()
# print("随机数组：",random_array)

#--------------------------------------------
# 排序算法									|
#											|
# 稳定性：									|
#   原有相等值的相对次序不变		
#
#
# 1.冒泡排序
# 2.选择排序
# 3.插入排序
# 4.希尔排序
# 5.快速排序
# 6.归并排序
# 7.堆排序
#
#--------------------------------------------

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



# Insertion Sort:
#
#
#
#   ⒈ 从第一个元素开始，该元素可以认为已经被排序
# 	⒉ 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 	⒊ 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 	⒋ 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 	⒌ 将新元素插入到下一位置中
# 	⒍ 重复步骤2~5
#
# 最优时间复杂度：O(n)
# 最差时间复杂度：O(n^2)
#

def insert_sort(array):
	length = len(array)
	for index in range(1,length):
		j = index-1
		element = array[index]
		while j >= 0:
			if array[j] > element:
				array[j+1] = array[j]
				array[j] = element
			j-=1
	return array


# Shell Sort: 
# 	插入排序的一种，直接插入排序的高效版本
# 	非稳定的排序算法
#

def shell_sort(array):
	n = len(array) 
	gap = n // 2
	for j in range(gap,n):
		i = j
		while i > 0:
			if array[i] < array[i-gap]:
				array[i],array[i-gap] = array[i-gap],array[i]
				i -= gap
			else:
				break
	return array

# Quick Sort:
#	快速排序
#
#

def quick_sort(array,first,last):

	if first >= last:
		return
	middle = array[first]
	low = first
	high = last
	while low < high:
		# high 左移
		while  low < high and array[high] >= middle:
			high -= 1
		array[low] = array[high]
		while low < high and array[low] < middle:
			low += 1
		array[low] = middle
	array[low] = middle

	quick_sort(array,first,low-1)
	quick_sort(array,low+1,last)
	return array


# Merge Sort
#
#
# 最优时间复杂度：O(nlogn)
# 最差时间复杂度：O(nlogn)
#
#

def merge_sort(array):
	n = len(array)
	if n <= 1:
		return array
	middle = n // 2
	left_list = merge_sort(array[:middle])
	right_list = merge_sort(array[middle:])

	left_pointer,right_pointer = 0,0
	result = []
	while  left_pointer < len(left_list) and right_pointer < len(right_list):
		if left_list[left_pointer] < right_list[right_pointer]:
			result.append(left_list[left_pointer])
			left_pointer += 1
		else:
			result.append(right_list[right_pointer])
			right_pointer += 1

	result += left_list[left_pointer:]
	result += right_list[right_pointer:]
	return result


a = merge_sort(random_array)
print(a)






	

