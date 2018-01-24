import time 
import platform


def system_message(): # 获取系统的信息，这也是我机器的运行信息
    print(platform.platform())       #获取操作系统名称及版本号
    print(platform.version())         #获取操作系统版本号，
    print(platform.architecture())    #获取操作系统的位数，
    print(platform.machine())         #计算机类型，
    print(platform.node())            #计算机的网络名称，
    print(platform.processor())       #计算机处理器信息，
#  测试使用的机器数据：	
#   Darwin-17.3.0-x86_64-i386-64bit
#   Darwin Kernel Version 17.3.0: Thu Nov  9 18:09:22 PST 2017; root:xnu-4570.31.3~1/RELEASE_X86_64
#   ('64bit', '')
#   x86_64
#   HH.local
#   i386

 # system_message()

#  			 .───────.      
# 		  ,─'         '─.   
#        ╱     .───.     ╲  
#       ╱    ,'     `.    ╲ 
#      ;    ;         :    :
#      │    │         │    │
#      │    │         │    │
#      ______.        ;    ;
#                    ╱    ╱ 
#                 ,'    ╱  
#              │─'     ╱   
#              ┌┘    ,─'    
#              ▼───┬'       
#              │   │        
#              │   │        
#              │   │        
#              │   │        
#              │   │        
#              │   │        
#              │   │        
#              │   │        
#              └───┘        
#              ┌───┐        
#              │   │        
#              └───┘   
#
# a+b+c=1000 a^2+b^2=c^2 求满足的a,b,c

def pure_enum_way(max_number): # 纯粹枚举
	i=1
	for a in range(0,max_number+1):
		for b in range(0,max_number+1):
			for c in range(0,max_number+1):
				i=i+1
				print(i)
				if a+b+c==max_number and a**2+b**2==c**2:
					print(a,b,c)
# T = 1000*1000*1000*2
# 做了10**9次 比较
# 耗时：123.7910509109497 


def half_enum_way(max_number):
	for a in range(0,max_number+1):
		for b in range(0,max_number+1):
			c = max_number-a-b
			if a+b+c==max_number and a**2+b**2==c**2:
				print(a,b,c)
# T = 1000*1000*2
# 做了1002002次比较
# 耗时： 1.3410487174987793 


def accurate_enum_way(max_number):
	for a in range(0,max_number+1):
		for b in range(0,max_number+1-a):
			if (a**2+b**2 == (max_number-a-b)**2):
				print(a,b,max_number-a-b)

def elapsed_time(func,max_number,func_name):
	start_time = time.time()
	func(max_number)
	print("%s use time:%s " % (func_name,time.time()-start_time))	
# T = 1000
# 做了 501501 次比较
# 0.5968608856201172 

max_number = 10000
# elapsed_time(pure_enum_way,max_number,"Pure way")
# elapsed_time(half_enum_way,max_number,"Half way")
elapsed_time(accurate_enum_way,max_number,"Accurate way")

# max_number = 10000
# 0 5000 5000
# 2000 3750 4250
# 3750 2000 4250
# 5000 0 5000
# Half way use time:137.7435278892517 

#total = pure_enum_way(1000)
#print(total)
# half_enum_way(10000)
