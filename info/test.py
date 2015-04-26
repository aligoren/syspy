from info import Info

inf = Info()

def user():
	"""
	Username: ali Terminal: None Host: 0.0.0.0 Start Time: 2015-04-26 15:10:30
	"""
	a,b,c,d = inf.getUsers()

	print("Username: {} Terminal: {} Host: {} Start Time: {}".format(a,b,c,d))

def boot():
	"""
	Boot Time: 2015-04-26 15:10:13
	"""
	a = inf.getBootTime()
	print("Boot Time: {0}".format(a))

def iterprocess():
	"""
		{'name': 'DTLite.exe', 'pid': 1108}
		{'name': None, 'pid': 1140}
		{'name': None, 'pid': 1172}
		{'name': None, 'pid': 1188}
		{'name': None, 'pid': 1272}
		{'name': None, 'pid': 1296}
		{'name': None, 'pid': 1336}
		{'name': None, 'pid': 1372}
		{'name': None, 'pid': 1380}
		{'name': 'chrome.exe', 'pid': 1464}
		{'name': None, 'pid': 1520}
		{'name': 'taskhost.exe', 'pid': 1536}
		{'name': None, 'pid': 1656}
		{'name': None, 'pid': 1664}
		{'name': None, 'pid': 1752}
		{'name': None, 'pid': 1796}
		{'name': None, 'pid': 1808}
		{'name': 'chrome.exe', 'pid': 1828}
		{'name': 'GCTray.exe', 'pid': 1832}
	"""
	piter = inf.getProcessIter()
	print("{0}".format(piter))

#user()
#boot()
#iterprocess()