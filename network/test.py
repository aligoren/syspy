from network import Network

nw = Network()

def netIoCounters():
	"""
		Bytes Sent: 11.6M
		Bytes Recv: 191.0M
		Packets Sent: 104.9K
		Packets Recv: 163.7K
		Errin: 0B
		Errour: 0B
		Dropin: 0B
		Dropout: 0B
	"""
	a,b,c,d,e,f,g,h = nw.getNetIoCounters()

	print("Bytes Sent: {}\nBytes Recv: {}\nPackets Sent: {}\nPackets Recv: {}" \
		"\nErrin: {}\nErrour: {}\nDropin: {}\nDropout: {}".format(a,b,c,d,e,f,g,h))


def netConnections():
	"""
		Proto Local address                  Remote address                 Status        PID    Program name
		tcp   0.0.0.0:135                    -                              LISTEN        800    ?
		tcp   192.168.2.94:139               -                              LISTEN        4      System
		tcp   0.0.0.0:1025                   -                              LISTEN        488    ?
		tcp   0.0.0.0:1026                   -                              LISTEN        932    ?
		tcp   0.0.0.0:1027                   -                              LISTEN        1076   ?
		tcp   0.0.0.0:1028                   -                              LISTEN        568    ?
		tcp   0.0.0.0:1029                   -                              LISTEN        544    ?
		tcp   192.168.2.94:3291              192.30.252.86:443              ESTABLISHED   3728   chrome.exe
	"""
	nw.getNetConnections()

#netIoCounters()
#netConnections()