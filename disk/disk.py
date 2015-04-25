import psutil
import os

class Disk:

	def __init__(self):
		self.bytes2human
		self.getDiskPartitions
		self.getDiskUsage
		self.getDiskIoCounters

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
		
	def getDiskPartitions(self):
		"""
		Return all mounted disk partitions as a list of namedtuples
		including device, mount point and filesystem type,
		similarly to “df” command on UNIX. If all parameter
		is False return physical devices only
		(e.g. hard disks, cd-rom drives, USB keys)
		and ignore all others (e.g. memory partitions such as /dev/shm).
		Namedtuple’s fstype field is a string which varies depending on the platform.
		On Linux it can be one of the values found in /proc/filesystems
		(e.g. 'ext3' for an ext3 hard drive o 'iso9660' for the CD-ROM drive).
		On Windows it is determined via GetDriveType and can be either
		"removable", "fixed", "remote", "cdrom", "unmounted" or "ramdisk".
		On OSX and FreeBSD it is retrieved via getfsstat(2).
		"""
		for part in psutil.disk_partitions(all=False):
			if os.name == 'nt':
				if 'cdrom' in part.opts or part.fstype == '':
					continue
			
			usage = psutil.disk_usage(part.mountpoint)
			ret_pd = part.device
			ret_ut = self.bytes2human(usage.total)
			ret_usu = self.bytes2human(usage.used)
			ret_ufree = self.bytes2human(usage.free)
			ret_uper = int(usage.percent)
			ret_prt = part.fstype
			ret_pmoup = part.mountpoint

			return ret_pd, ret_ut, ret_usu, ret_ufree, ret_uper, ret_prt, ret_pmoup

	def getDiskUsage(self):
		"""
		Return disk usage statistics about the given path as a namedtuple including total,
		used and free space expressed in bytes, plus the percentage usage.
		OSError is raised if path does not exist
		"""
		dusage = list(psutil.disk_usage('/'))

		ret_total = self.bytes2human(dusage[0])
		ret_used = self.bytes2human(dusage[1])
		ret_free = self.bytes2human(dusage[2])
		ret_percent = dusage[3]

		return ret_total, ret_used, ret_free, ret_percent

	def getDiskIoCounters(self):
		"""
		Return system-wide disk I/O statistics as a namedtuple including the following fields:

		read_count: number of reads
		write_count: number of writes
		read_bytes: number of bytes read
		write_bytes: number of bytes written
		read_time: time spent reading from disk (in milliseconds)
		write_time: time spent writing to disk (in milliseconds)
		"""
		dioc = list(psutil.disk_io_counters())

		ret_read_count = dioc[0]
		ret_write_count = dioc[1]
		ret_read_bytes = dioc[2]
		ret_write_bytes = dioc[3]
		ret_read_time = dioc[4]
		ret_write_time = dioc[5]

		return ret_read_count, ret_write_count, ret_read_bytes, ret_write_bytes, ret_read_time, ret_write_time