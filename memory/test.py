from memory import Memory

mem = Memory()

def virtualMem():
	"""
	START Test Results

		Total: 2.0G Available: 912.5M Percent: 55.3 Used: 1.1G Free: 912.5M
	
	END Test Results
	
	START return values
	
	a = total
	b = available
	c = percent
	d = used
	e = free

	END return values
	"""
	a,b,c,d,e = mem.getVirtualMemory()

	print("Total: {0} Available: {1} Percent: {2} Used: {3} Free: {4}".format(a,b,c,d,e))

def swapMem():
	"""
	START Test Results

		Total: 4.0G Used: 1.7G Free: 2.3G Percent: 42.3 Sin: 0B Sout: 0B
	
	END Test Results

	START return values

	a = total swap memory
	b = used swap memory
	c = free swap memory
	d = swap memory percent
	d = the number of bytes the system has swapped in from disk
	e = the number of bytes the system has swapped out from disk
	
	END return values
	"""
	a,b,c,d,e,f = mem.getSwapMemory()
	print("Total: {0} Used: {1} Free: {2} Percent: {3} Sin: {4} Sout: {5}".format(a,b,c,d,e,f))

def memoryInfo():
	"""
	START Test Results

	RSS: 8.1M VMS: 5.3M
	
	END Test Results
	
	START return values

	a = RSS(Resident Set Size)
	b = VMS(Virtual Memory Size)

	END return values
	"""
	a,b = mem.getMemoryInfo()
	print("RSS: {0} VMS: {1}".format(a,b))

def memoryInfoEx():
	"""
	START Test Results

		num_page_faults: 2.2K
		peak_wset: 8.0M
		wset: 8.0M
		peak_paged_pool: 98.6K
		paged tools: 98.6K
		peak_nonpaged_pool: 4.4K
		nonpaged_pool: 4.4K
		pagefile: 5.2M
		peak_pagefile: 5.2M
		private: 5.2M

	END Test Results

	START return values
	
	a = num_page_faults
	b = peak_wset
	c = wset
	d = peak_paged_pool
	e = paged_tool
	f = peak_nonpaged_pool
	g = nonpaged_pool
	h = pagefile
	i = peak_pagefile
	j = private

	http://pythonhosted.org/psutil/#psutil.Process.memory_info_ex

	END return values
	"""
	a,b,c,d,e,f,g,h,i,j = mem.getMemoryInfoEx()

	print("num_page_faults: {0}\npeak_wset: {1}\nwset: {2}\npeak_paged_pool: {3}\n" \
		"paged_tool: {4}\npeak_nonpaged_pool: {5}\nnonpaged_pool: {6}\n" \
		"pagefile: {7}\npeak_pagefile: {8}\nprivate: {9}".format(a,b,c,d,e,f,g,h,i,j))


def memoryPercent():
	"""
	START Test Results

		Memory Percent: 0.3964004619891539
	
	END Test Results
	"""
	mpercent = mem.getMemoryPercent()
	print("Memory Percent: {0}".format(mpercent))

def memoryMap():
	"""
	START Test Results
		PID: 6128
		Name: conhost.exe
		RSS: 4.0K
		Permission: r
		Path: C:\Windows\System32\apisetschema.dll
		Total RSS: 24.5M
	END Test Results

	START return values
	
	PID: Process ID
	NAME: Process Name
	RSS: Resident Set Size
	Permission: Process Permission
	Path: Process Api Path
	Total RSS: Total Resident Set Size
	
	END	return values
	"""

	a,b,c,d,e,f =  mem.getMemoryMap(5128)
	print("PID: {0}\nName: {1}\nRSS: {2}\nPermission: {3}\nPath: {4}\nTotal RSS: {5}".format(a,b,c,d,e,f))

#virtualMem()
#swapMem()
#memoryInfo()
#memoryInfoEx()
#memoryPercent()
#memoryMap()