#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
password=getpass()

pynet1={
'device_type':'cisco_ios',
'ip':'50.76.53.27',
'username':'pyclass',
'password':password,
}

pynet2={
'device_type':'cisco_ios',
'ip':'50.76.53.27',
'username':'pyclass',
'password':password,
'port': 8022,
}


juniper_srx = {
 'device_type':'juniper',
 'ip':'50.76.53.27',
 'username':'pyclass',
 'password': password,
 'secret':'',
 'port': 9822, 
}

rtr1=ConnectHandler(**pynet1)
rtr2=ConnectHandler(**pynet2)
srx=ConnectHandler(**juniper_srx)


print rtr1.find_prompt()
rtr1.config_mode()
rtr1.exit_config_mode()
print rtr1.send_command('show ip int brief')
print rtr1.send_command('show run | inc logging buffered')
config_set=['logging buffered 65000']
print rtr1.send_config_set(config_set)
print rtr1.send_command('show run | inc logging buffered')
print dir(rtr1)
