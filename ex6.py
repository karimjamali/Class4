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


print '\n\n pynet-rtr1 arp table is \n', rtr1.send_command('show arp')
print '\n\npynet-rtr2 arp table is \n',rtr2.send_command('show arp')
print '\n\n srx arp table is \n' ,srx.send_command('show arp')
#config_set=['logging buffered 65000']
#print rtr1.send_config_set(config_set)
#print rtr1.send_command('show run | inc logging buffered')
#print dir(rtr1)
