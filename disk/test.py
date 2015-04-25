from disk import Disk

dsc = Disk()

def diskPartitions():
	"""
		Part Device: C:\
		Usage Total: 113.4G
		Usage Used: 57.8G
		Usage Free: 55.6G
		Usage Percent: 50
		Part Type: NTFS
		Part Mountpoint: C:\
	"""
	a,b,c,d,e,f,g = dsc.getDiskPartitions()

	print("Part Device: {}\nUsage Total: {}\nUsage Used: {}\nUsage Free: {}" \
			"\nUsage Percent: {}\nPart Type: {}\nPart Mountpoint: {}".format(a,b,c,d,e,f,g))

def diskUsage():
	"""
	Total: 113.4G Used: 57.7G Free: 55.6G Percent: 50.9
	"""
	a,b,c,d = dsc.getDiskUsage()
	print("Total: %s Used: %s Free: %s Percent: %s" % (a,b,c,d))


def diskIoCounters():
	"""
	Read Count: 442404
	Write Count: 246040
	Read Bytes: 13650447872
	Write Bytes: 4814406656
	Read Times: 649029420 ms
	Write Time: 57618720 ms
	"""
	a,b,c,d,e,f = dsc.getDiskIoCounters()
	print("Read Count: %s\nWrite Count: %s\nRead Bytes: %s\nWrite Bytes: %s\nRead Times: %s ms\nWrite Time: %s ms"
		% (a,b,c,d,e,f))


#diskPartitions()
#diskUsage()
diskIoCounters()