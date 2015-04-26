__title__ = 'syspy'
__version__ = '0.1'
__author__ = 'Ali GOREN <goren.ali@yandex.com>'
__repo__ = 'https://github.com/aligoren/syspy'
__license__ = 'Apache v2.0 License'

import psutil
import datetime

class Info:

	def __init__(self):
		self.getUsers
		self.getBootTime
		self.getProcessIter

	def getUsers(self):
		"""
		Return users currently connected on the system as a list of namedtuples including the following fields:

		user: the name of the user.
		terminal: the tty or pseudo-tty associated with the user, if any, else None.
		host: the host name associated with the entry, if any.
		started: the creation time as a floating point number expressed in seconds since the epoch.

			>>> import psutil
			>>> psutil.users()
			[suser(name='ali', terminal=None, host='0.0.0.0', started=1430050230.0)]
			>>> lusers = list(psutil.users())
			>>> lusers
			[suser(name='ali', terminal=None, host='0.0.0.0', started=1430050230.0)]
			>>> lusers[0]
			suser(name='ali', terminal=None, host='0.0.0.0', started=1430050230.0)
			>>> lusers[0][1]
			>>> lusers[0][0]
			'ali'
			>>> lusers[0][3]
			1430050230.0
			>>> lusers[0][3]..strftime("%Y-%m-%d %H:%M:%S")
			  File "<stdin>", line 1
			    lusers[0][3]..strftime("%Y-%m-%d %H:%M:%S")
			                 ^
			SyntaxError: invalid syntax
			>>> lusers[0][3].strftime("%Y-%m-%d %H:%M:%S")
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			AttributeError: 'float' object has no attribute 'strftime'
			>>> import datetime
			>>> datetime.datetime.fromtimestamp(lusers[0][3].strftime("%Y-%m-%d %H:%M:%S"))
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			AttributeError: 'float' object has no attribute 'strftime'
			>>>
		"""
		lusers = psutil.users()

		ret_user_name = lusers[0][0]
		ret_user_terminal = lusers[0][1]
		ret_user_host = lusers[0][2]
		ret_start_time = datetime.datetime.fromtimestamp(lusers[0][3]).strftime("%Y-%m-%d %H:%M:%S")

		return ret_user_name, ret_user_terminal, ret_user_host, ret_start_time

	def getBootTime(self):
		"""
		Return the system boot time expressed in seconds since the epoch.
		"""
		btime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

		return btime

	def getProcessIter(self):
		"""
		Return an iterator yielding a Process class instance for all running processes on the local machine.
		Every instance is only created once and then cached into an internal
		table which is updated every time an element is yielded.
		Cached Process instances are checked for identity so that you’re
		safe in case a PID has been reused by another process,
		in which case the cached instance is updated.
		This is should be preferred over psutil.pids() for iterating over processes.

			>>> for proc in psutil.process_iter():
			...     try:
			...             pinfo = proc.as_dict(attrs=['pid', 'name'])
			...     except psutil.NoSuchProcess:
			...             pass
			...     else:
			...             print(pinfo)
			...
			{'pid': 0, 'name': 'System Idle Process'}
			{'pid': 4, 'name': 'System'}
			{'pid': 216, 'name': None}
			{'pid': 252, 'name': None}
			{'pid': 404, 'name': None}
			{'pid': 488, 'name': None}
			{'pid': 500, 'name': None}
			{'pid': 544, 'name': None}
			{'pid': 568, 'name': None}
		"""
		for proc in psutil.process_iter():
			try:
				pinfo = proc.as_dict(attrs=['pid', 'name'])
			except psutil.NoSuchProcess:
				pass
			else:
				print(pinfo)