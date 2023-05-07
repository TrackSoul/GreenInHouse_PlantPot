#import commands
import datetime
import psutil
import subprocess
from datetime import timedelta

class Raspberry:

    @staticmethod
    def get_cpuload():
        cpuload = psutil.cpu_percent(interval=1, percpu=False)
        return str(cpuload)

    @staticmethod
    def get_ram():
        san = subprocess.check_output(['free','-m'])
        lines = san.split(b'\n')
        return ( int(lines[1].split()[1]), int(lines[2].split()[3]) )

    @staticmethod
    def get_cpu_temp():
        tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
        cpu_temp = tempFile.read()
        tempFile.close()
        return float(cpu_temp)/1000

    '''
    @staticmethod
    def get_gpu_temp():
        gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace('temp=','').replace('C','')
        return float(gpu_temp)
    '''

    @staticmethod
    def get_connections():
        san = subprocess.check_output(['netstat','-tun'])
        return len([x for x in san.split() if x == 'ESTABLISHED'])

    @staticmethod
    def get_ipaddress():
        arg='ip route list'
        ip=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
        data = ip.communicate()
        split_data = data[0].split()
        ipaddr = split_data[split_data.index(b'src')+1]
        return ipaddr

    @staticmethod
    def get_uptime():
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime = (timedelta(seconds = uptime_seconds))
        return str(uptime)
    
    @staticmethod
    def print_statistics():
        print( 'Uso CPU  ' + Raspberry.get_cpuload() + '%')
        print(  'Mem. Libre ' + str(Raspberry.get_ram()[1])+ ' Mbytes')
        print(  'Temp.CPU ' + str(Raspberry.get_cpu_temp()))
        #print(  'Temp.GPU ' + str(Raspberry.get_gpu_temp()))
        print(  'Con.Red. ' + str(Raspberry.get_connections())+ ' Activas')
        print( 'Direc.IP ' + str(Raspberry.get_ipaddress())+ ' ')
        print( 'Uptime   ' + Raspberry.get_uptime())

Raspberry.print_statistics()