import psutil

class CPU:

	def __init__(self):

		self.getCpuTimes
		self.getCpuPercent
		self.cpuPercentPerCpu
		self.cpuTimesPercent
		self.getCpuCount
		self.getCpuAffinity


	def getCpuTimes(self):
		"""
		START listCpuValues
			
			http://stackoverflow.com/a/10058239/3821823
			dict.items would return an iterable dict view object rather than a list.
			We need to wrap the call onto a list in order to make the indexing possible
		
		END listCpuValues

		START Test Results
			
			>>> import psutil
			>>> a = psutil.cpu_times()
			>>> a.items()
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			AttributeError: 'scputimes' object has no attribute 'items'
			>>> b = a.__dict_
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			AttributeError: 'scputimes' object has no attribute '__dict_'
			>>> b = a.__dict__
			>>> b.items()
			ItemsView(OrderedDict([('user', 822.62451171875), ('system', 373.341796875), ('i
			dle', 21677.9609375)]))
			>>> list(b.items())
			[('user', 822.62451171875), ('system', 373.341796875), ('idle', 21677.9609375)]
			>>> list(b.items())[0]
			('user', 822.62451171875)
			>>> list(b.items())[0][1]
			822.62451171875
			>>> ass = list(b.items())
			>>> ass[0][1]
			822.62451171875
			>>> ass[1][1]
			373.341796875
			>>> ass[2][1]
			21677.9609375
			>>> psutil.cpu_times()
			scputimes(user=934.0092163085938, system=431.310546875, idle=23977.853515625)
			>>>
		
		END Test Results

		START return values
		
			https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch07s04.html
		
		END return values
		"""
		cpuToDict = psutil.cpu_times()
		cpuDict = cpuToDict.__dict__
		listCpuValues = list(cpuDict.items())

		ret_val_user = "{0}".format(listCpuValues[0][1])
		ret_val_system = "{0}".format(listCpuValues[1][1])
		ret_val_idle = "{0}".format(listCpuValues[2][1])

		return ret_val_user, ret_val_system, ret_val_idle

	def getCpuPercent(self):
		"""
		START Test Results

			>>> import psutil
			>>> psutil.cpu_percent(interval=1)
			0.7
			>>> for x in range(6):
			...     psutil.cpu_percent(interval=1)
			...
			0.0
			0.9
			0.0
			0.0
			0.8
			0.0

		END Test Results
		"""
		currentCpuPercent = psutil.cpu_percent(interval=1)
		
		return currentCpuPercent

	def cpuPercentPerCpu(self):
		"""
		START Test Results
			
			>>> import psutil
			>>> for i in range(3):
			...     psutil.cpu_percent(interval=1,percpu=True)
			...
			[0.0, 1.6]
			[0.1, 0.0]
			[0.0, 0.1]
			>>> a = psutil.cpu_percent(interval=1,percpu=True)
			>>> a[0]
			0.0
			>>> a[0][1]
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			TypeError: 'float' object is not subscriptable
			>>> a[0][0]
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			TypeError: 'float' object is not subscriptable
			>>> list(a)
			[0.0, 0.0]
			>>> list(a)[0]
			0.0
			>>> list(a)[1]
			0.0
			>>> for i in range(3):
			...     a = psutil.cpu_percent(interval=1,percpu=True)
			...     list(a[i][i])
			...
			Traceback (most recent call last):
			  File "<stdin>", line 3, in <module>
			TypeError: 'float' object is not subscriptable
			>>>
		
		END Test Results
		"""
		cpuPerCpuPercent = psutil.cpu_percent(interval=1, percpu=True)

		return cpuPerCpuPercent

	def cpuTimesPercent(self):
		"""
		START Test Results
			
			>>> import psutil
			>>> for x in range(4):
			...     psutil.cpu_times_percent(interval=1, percpu=False)
			...
			scputimes(user=6.9, system=0.0, idle=93.1)
			scputimes(user=0.0, system=0.9, idle=99.1)
			scputimes(user=0.0, system=0.0, idle=100.0)
			scputimes(user=0.0, system=0.0, idle=100.0)
			>>> for x in range(4):
			...     psutil.cpu_times_percent(interval=1, percpu=True)
			...
			[scputimes(user=0.0, system=0.0, idle=100.0), scputimes(user=0.0, system=0.1, id
			le=99.9)]
			[scputimes(user=0.0, system=1.4, idle=98.6), scputimes(user=0.0, system=0.0, idl
			e=100.0)]
			[scputimes(user=0.0, system=0.1, idle=99.9), scputimes(user=0.0, system=0.0, idl
			e=100.0)]
			[scputimes(user=0.0, system=0.0, idle=100.0), scputimes(user=0.0, system=1.5, id
			le=98.5)]
			>>> a = psutil.cpu_times_percent(interval=1 percpu=False)
			  File "<stdin>", line 1
			    a = psutil.cpu_times_percent(interval=1 percpu=False)
			                                                 ^
			SyntaxError: invalid syntax
			>>> a = psutil.cpu_times_percent(interval=1, percpu=False)
			>>> list(a)
			[0.0, 0.0, 100.0]
			>>> ab = list(a)
			>>> ab[0]
			0.0
			>>> ab[1]
			0.0
			>>> ab[2]
			100.0
			>>> ab.items()
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			AttributeError: 'list' object has no attribute 'items'
			>>> a = psutil.cpu_times_percent(interval=1, percpu=True)
			>>> ab = list(a)
			>>> ab[0]
			scputimes(user=0.0, system=0.0, idle=100.0)
			>>> ab[0][1]
			0.0
			>>> ab[0][2]
			100.0
			>>> ab[0][0]
			0.0
			>>>
		
		END Test Results
		"""
		timesPercent = psutil.cpu_times_percent(interval=1, percpu=False)
		percentList = list(timesPercent)

		ret_val_user = "{0}".format(percentList[0])
		ret_val_system = "{0}".format(percentList[1])
		ret_val_idle = "{0}".format(percentList[2])

		return ret_val_user, ret_val_system, ret_val_idle

	def getCpuCount(self):
		"""
		START Test Results
			
			>>> import psutil
			>>> psutil.cpu_count()
			2
			>>> psutil.cpu_count(logical=False)
			2
			>>> psutil.cpu_count(logical=True)
			2
			>>>
		
		END Test Results
		"""
		cpuCount = "{0}".format(psutil.cpu_count())
		cpuCountLogicalFalse = "{0}".format(psutil.cpu_count(logical=False))

		return cpuCount, cpuCountLogicalFalse

	def getCpuAffinity(self):
		"""
		START Test Results

			>>> import psutil
			>>> p = psutil.Process()
			>>> p.cpuaffinity()
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			AttributeError: 'Process' object has no attribute 'cpuaffinity'
			>>> p.cpu_affinity()
			[0, 1]
			>>> p.cpu_affinity()
			[0, 1]
			>>> p.cpu_affinity()
			[0, 1]
			>>> a = list(range(psutil.cpu_count()))
			>>> p.cpu_affinity(a)
			>>> p.cpu_affinity()
			[0, 1]
			>>> p.cpu_affinity(a)
			>>>

		END Test Results
		"""
		cAffinity = psutil.Process()
		c_affinity = "{0}".format(cAffinity.cpu_affinity())

		return c_affinity


