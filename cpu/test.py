from cpu import CPU

cps = CPU()

def cpuTime():
	"""
	START Test Results

	User: 1076.952880859375 System: 534.6328125 IDLE: 29336.767578125

	a = user cpu times
	b = system cpu times
	c = idle cpu times

	END Test Results
	"""
	a,b,c = cps.getCpuTimes()

	print("User: {0} System: {1} IDLE: {2}".format(a,b,c))

def cpuPercent():
	""" 
	START Test Results

	For 10 times:
	Current CPU Usage: 0.0
	Current CPU Usage: 0.0
	Current CPU Usage: 0.0
	Current CPU Usage: 0.8
	Current CPU Usage: 0.0
	Current CPU Usage: 0.1
	Current CPU Usage: 1.5
	Current CPU Usage: 0.0
	Current CPU Usage: 0.0
	Current CPU Usage: 0.8

	END Test Results
	"""
	for i in range(5):
		print("Current CPU Usage: {0}".format(cps.getCpuPercent()))

def cpuPercentPerCpu():
	"""
	START Test Results

	For two processors
	Cpu Percent Per Cpu: [7.9, 4.8]
	Cpu Percent Per Cpu: [29.2, 29.2]
	Cpu Percent Per Cpu: [1.6, 0.0]
	Cpu Percent Per Cpu: [0.0, 0.0]
	Cpu Percent Per Cpu: [0.0, 0.0]

	END Test Results
	"""
	for i in range(5):
		print("Cpu Percent Per Cpu: {0}".format(cps.cpuPercentPerCpu()))

def timesPercent():
	"""
	START Test Results

	CPU Times Percent:
	User: 0.0 System: 0.0 IDLE: 100.0
	
	a = user cpu times percent
	b = system cpu times percent
	c = idle cpu times percent
	
	END Test Results
	"""
	a, b, c = cps.cpuTimesPercent()
	print("CPU Times Percent: \nUser: {0} System: {1} IDLE: {2}".format(a,b,c))

def processorCount():
	"""
	START Test Results

	Cpu Count: 2
	Cpu Count without Logical: 2

	a = Totally Cpu Count
	b = Without logical

	END Test Results
	"""
	a,b = cps.getCpuCount()
	print("Cpu Count: {0}\nCpu Count without Logical: {1}".format(a,b))

def caffinity():
	"""
	START Test Results

	CPU Affinity: [0, 1]

	END Test Results
	"""
	caffinityTest = cps.getCpuAffinity()
	print("CPU Affinity: {0}".format(caffinityTest))


#cpuTime()
#cpuPercent()
#cpuPercentPerCpu()
#timesPercent()
#processorCount()
#caffinity()