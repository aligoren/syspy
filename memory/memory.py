__title__ = 'syspy'
__version__ = '0.1'
__author__ = 'Ali GOREN <goren.ali@yandex.com>'
__repo__ = 'https://github.com/aligoren/syspy'
__license__ = 'Apache v2.0 License'

import psutil

class Memory:

	def __init__(self):
		self.bytes2human
		self.getVirtualMemory
		self.getSwapMemory
		self.getMemoryInfo
		self.getMemoryInfoEx
		self.getMemoryPercent
		self.getMemoryMap

	def bytes2human(self,n):
		    # http://code.activestate.com/recipes/578019
		    # >>> bytes2human(10000)
		    # '9.8K'
		    # >>> bytes2human(100001221)
		    # '95.4M'
		    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
		    prefix = {}
		    for i, s in enumerate(symbols):
		        prefix[s] = 1 << (i + 1) * 10
		    for s in reversed(symbols):
		        if n >= prefix[s]:
		            value = float(n) / prefix[s]
		            return '%.1f%s' % (value, s)
		    return "%sB" % n
	
	def getVirtualMemory(self):
		"""
		START Test Results

			>>> import psutil
			>>> mem = psutil.virtual_memory()
			>>> mem
			svmem(total=2142027776, available=1013366784, percent=52.7, used=1128660992, free=1013366784)
			>>> lmem = list(mem)
			>>> lmem
			[2142027776, 1013366784, 52.7, 1128660992, 1013366784]
			>>> lmem[0]
			2142027776
			>>>
		
		END Test Results
		"""
		mem = psutil.virtual_memory()
		lmem = list(mem)

		ret_total = "{0}".format(self.bytes2human(lmem[0]))
		ret_ava = "{0}".format(self.bytes2human(lmem[1]))
		ret_percent = "{0}".format(lmem[2])
		ret_used = "{0}".format(self.bytes2human(lmem[3]))
		ret_free = "{0}".format(self.bytes2human(lmem[4]))

		return ret_total, ret_ava, ret_percent, ret_used, ret_free

	def getSwapMemory(self):
		"""
		START Test Results

			>>> import psutil
			>>> psutil.swap_memory()
			sswap(total=4284055552, used=1793249280, free=2490806272, percent=41.9, sin=0, s
			out=0)
			>>> smem = psutil.swap_memory()
			>>> lsmem = list(smem)
			>>> lsmem
			[4284055552, 1794441216, 2489614336, 41.9, 0, 0]
			>>>
		
		END Test Results
		"""
		smem = psutil.swap_memory()
		lsmem = list(smem)

		ret_swap_total = "{0}".format(self.bytes2human(lsmem[0]))
		ret_swap_used = "{0}".format(self.bytes2human(lsmem[1]))
		ret_swap_free = "{0}".format(self.bytes2human(lsmem[2]))
		ret_swap_percent = "{0}".format(lsmem[3])
		ret_swap_sin = "{0}".format(self.bytes2human(lsmem[4]))
		ret_swap_sout = "{0}".format(self.bytes2human(lsmem[5]))

		return ret_swap_total, ret_swap_used, ret_swap_free, ret_swap_percent, ret_swap_sin, ret_swap_sout

	def getMemoryInfo(self):
		"""
		START Test Results
			>>> import psutil
			>>> p = psutil.Process()
			>>> p.memory_info()
			pmem(rss=8536064, vms=5599232)
			>>> minfo = list(p.memory_info())
			>>> minfo
			[8613888, 5672960]
			>>>
		END Test Results

		START return values
		
			ret_rss = RSS(Resident Set Size)
			ret_vms = VMS(Virtual Memory Size)
		
		END return values
		"""
		p = psutil.Process()

		minfo = list(p.memory_info())

		ret_rss = "{0}".format(self.bytes2human(minfo[0]))
		ret_vms = "{0}".format(self.bytes2human(minfo[1]))

		return ret_rss, ret_vms

	def getMemoryInfoEx(self):
		"""
		START Test Results
			>>> import psutil
			>>> p = psutil.Process()
			>>> p.memory_info_ex()
			pextmem(num_page_faults=2277, peak_wset=8552448, wset=8552448, peak_paged_pool=1
			00980, paged_pool=100980, peak_nonpaged_pool=4484, nonpaged_pool=4484, pagefile=
			5607424, peak_pagefile=5607424, private=5607424)
			>>> minfo = list(p.memory_info_ex())
			>>> minfo
			[2297, 8634368, 8634368, 100980, 100980, 4844, 4844, 5681152, 5681152, 5681152]
			>>>
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
		p = psutil.Process()

		minfo_ex = list(p.memory_info_ex())

		ret_faults = "{0}".format(self.bytes2human(minfo_ex[0]))
		ret_peak_wset = "{0}".format(self.bytes2human(minfo_ex[1]))
		ret_wset = "{0}".format(self.bytes2human(minfo_ex[2]))
		ret_peak_ptool = "{0}".format(self.bytes2human(minfo_ex[3]))
		ret_paged_tool = "{0}".format(self.bytes2human(minfo_ex[4]))
		ret_peak_nptool = "{0}".format(self.bytes2human(minfo_ex[5]))
		ret_nonpaged_tool = "{0}".format(self.bytes2human(minfo_ex[6]))
		ret_pagefile = "{0}".format(self.bytes2human(minfo_ex[7]))
		ret_peak_pfile = "{0}".format(self.bytes2human(minfo_ex[8]))
		ret_private = "{0}".format(self.bytes2human(minfo_ex[9]))

		return ret_faults, ret_peak_wset, ret_wset, ret_peak_ptool, ret_paged_tool, \
		ret_peak_nptool, ret_nonpaged_tool, ret_pagefile, ret_peak_pfile, ret_private

	def getMemoryPercent(self):
		"""
		START Test Results

			>>> import psutil
			>>> p = psutil.Process()
			>>> p.memory_percent()
			0.3954443586076075
			>>> list(p.memory_percent())
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			TypeError: 'float' object is not iterable
			>>>
		
		END Test Results
		"""
		p = psutil.Process()

		mpercent = p.memory_percent()

		ret_mpercent = "{0}".format(mpercent)

		return ret_mpercent

	def getMemoryMap(self,poid):
		"""
		START Test Results
			PID: 5128
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
		p = psutil.Process(int(poid))
		ret_pid = "{0}".format(p.pid)
		ret_name = "{0}".format(p.name())
		total_rss = 0
		for m in p.memory_maps(grouped=False):
			total_rss += m.rss
			ret_rss = "{0}".format(self.bytes2human(m.rss))
			ret_perm = "{0}".format(m.perms)
			ret_path = "{0}".format(m.path)
			ret_total = "{0}".format(self.bytes2human(total_rss))

		return ret_pid, ret_name, ret_rss, ret_perm, ret_path, ret_total