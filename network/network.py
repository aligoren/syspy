__title__ = 'syspy'
__version__ = '0.1'
__author__ = 'Ali GOREN <goren.ali@yandex.com>'
__repo__ = 'https://github.com/aligoren/syspy'
__license__ = 'Apache v2.0 License'

import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

import psutil



AD = "-"
AF_INET6 = getattr(socket, 'AF_INET6', object())
proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}


class Network:

	def __init__(self):
		self.bytes2human
		self.getNetIoCounters
		self.getNetConnections

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

	def getNetIoCounters(self):
		"""

		Return system-wide network I/O statistics as a namedtuple including the following attributes:

		bytes_sent: number of bytes sent
		bytes_recv: number of bytes received
		packets_sent: number of packets sent
		packets_recv: number of packets received
		errin: total number of errors while receiving
		errout: total number of errors while sending
		dropin: total number of incoming packets which were dropped
		dropout: total number of outgoing packets which were dropped (always 0 on OSX and BSD)
		If pernic is True return the same information for every network interface installed on
		the system as a dictionary with network interface names
		as the keys and the namedtuple described above as the values.

			>>> import psutil
			>>> ln = list(psutil.net_io_counters())
			>>> ln
			[11198193, 173143520, 95172, 148624, 0, 0, 0, 0]
			>>> ln = list(psutil.net_io_counters(pernic=True))
			>>> ln
			['Loopback Pseudo-Interface 1', 'Kablosuz A', 'Yerel A']
			>>> psutil.net_io_counters(pernic=True)
			{'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=
			0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'Kablosuz A': snetio
			(bytes_sent=11286740, bytes_recv=176409663, packets_sent=96451, packets_recv=150
			833, errin=0, errout=0, dropin=0, dropout=0), 'Yerel A': snetio(bytes_sent=0, by
			tes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout
			=0)}
			>>> psutil.net_io_counters()
			snetio(bytes_sent=11510800, bytes_recv=179194110, packets_sent=98058, packets_re
			cv=153191, errin=0, errout=0, dropin=0, dropout=0)
			>>>
		"""
		lnic = list(psutil.net_io_counters())

		ret_byte_sent = self.bytes2human(lnic[0])
		ret_byte_recv = self.bytes2human(lnic[1])
		ret_packets_sent = self.bytes2human(lnic[2])
		ret_packets_recv = self.bytes2human(lnic[3])
		ret_errin = self.bytes2human(lnic[4])
		ret_errout = self.bytes2human(lnic[5])
		ret_dropin = self.bytes2human(lnic[6])
		ret_dropout = self.bytes2human(lnic[7])

		return ret_byte_sent, ret_byte_recv, ret_packets_sent, ret_packets_recv, ret_errin, ret_errout, \
				ret_dropin, ret_dropout


	def getNetConnections(self):
		"""
		Return system-wide socket connections as a list of namedutples. Every namedtuple provides 7 attributes:

		fd: the socket file descriptor, if retrievable, else -1.
		If the connection refers to the current process this may be passed to socket.fromfd() to obtain a usable socket object.
		family: the address family, either AF_INET, AF_INET6 or AF_UNIX.
		type: the address type, either SOCK_STREAM or SOCK_DGRAM.
		laddr: the local address as a (ip, port) tuple or a path in case of AF_UNIX sockets.
		raddr: the remote address as a (ip, port) tuple or an absolute path in case of UNIX sockets.
		When the remote endpoint is not connected you’ll get an empty tuple (AF_INET*) or None (AF_UNIX).
		On Linux AF_UNIX sockets will always have this set to None.
		status: represents the status of a TCP connection.
		The return value is one of the psutil.CONN_* constants (a string).
		For UDP and UNIX sockets this is always going to be psutil.CONN_NONE.
		pid: the PID of the process which opened the socket, if retrievable, else None.
		On some platforms (e.g. Linux) the availability of this field changes depending on process privileges (root is needed).
		The kind parameter is a string which filters for connections that fit the following criteria:

		Kind 	value	Connections using
		“inet”	IPv4 and IPv6
		“inet4”	IPv4
		“inet6”	IPv6
		“tcp”	TCP
		“tcp4”	TCP over IPv4
		“tcp6”	TCP over IPv6
		“udp”	UDP
		“udp4”	UDP over IPv4
		“udp6”	UDP over IPv6
		“unix”	UNIX socket (both UDP and TCP protocols)
		“all”	the sum of all the possible families and protocols
		To get per-process connections use Process.connections().
		"""
		templ = "%-5s %-30s %-30s %-13s %-6s %s"
		print(templ % (
			"Proto", "Local address", "Remote address", "Status", "PID",
			"Program name"))
		proc_names = {}
		for p in psutil.process_iter():
			try:
				proc_names[p.pid] = p.name()
			except psutil.Error:
				pass
		for c in psutil.net_connections(kind='inet'):
			laddr = "%s:%s" % (c.laddr)
			raddr = ""
			if c.raddr:
				raddr = "%s:%s" % (c.raddr)
			print(templ % (
				proto_map[(c.family, c.type)],
				laddr,
				raddr or AD,
				c.status,
				c.pid or AD,
				proc_names.get(c.pid, '?')[:15],
				))
