#Windows System Information Tool with Python

Windows sistem bilgilerini Python ile alırsınız. Aslında zaten var olan bir kütüphanenin daha da basitleştirilmiş halidir.

Kullanmadan önce eğer gerekli kütüphane yok ise onu kurmanız gerekli. **syspy**, gösterdiği verileri **psutil** ile sağlar.

~~~~{.python}
from syspy import CPU
from syspy import Disk
from syspy import Info
from syspy import Memory
from syspy import Network

cpu = CPU()

print(cpu.getCpuTimes())

disk = Disk()

a,b,c,d,e,f,g = disk.getDiskPartitions()

print("Part Device: {}\nUsage Total: {}\nUsage Used: {}\nUsage Free: {}" \
            "\nUsage Percent: {}\nPart Type: {}\nPart Mountpoint: {}".format(a,b,c,d,e,f,g))

info = Info()

print(info.getBootTime())

memory = Memory()

a,b,c,d,e,f = memory.getSwapMemory()
print("Total: {0} Used: {1} Free: {2} Percent: {3} Sin: {4} Sout: {5}".format(a,b,c,d,e,f))

network = Network()

print(network.getNetConnections())
~~~~

#Neleri Gösterir?

**CPU**:
    
    CPU Times, CPU Percent, CPU Percent Per CPU, CPU Percent Times, CPU Count, CPU Affinity

**Disk**:

    Disk Partitions, Disk Usage, Disk I/O Counters

**Information**:

    Users, Boot Time, Process Iteration Tool

**Memory**:

    Virtual Memory, Swap Memory, Memory Info, Memory Info(Extend), Memory Percent, Memory Map

**Network**:

    Network I/O Counters, Net Connections


Şimdilik bu özellikleri sağlamakta. Test dosyalarına bakabilirsiniz.

**Test Files**:

    cpu --
        \test.py
    disk --
        \test.py
    info --
        \test.py
    memory --
        \test.py
    network --
        \test.py 

#Kurulum
~~~~{.shell}
python setup.py install
~~~~

#Gereksinim Kurulumu

`pip install -r requirements.txt`