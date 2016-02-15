import paramiko
from getpass import getpass
import time

ip_addr='50.76.53.27'
username='pyclass'
password=getpass()
port = 22

remote_conn_pre=paramiko.SSHClient()

remote_conn_pre.load_system_host_keys()

#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#username = "pyclass"
#password = "88newclass"

#print dir(remote_conn_pre)

remote_conn_pre.connect(ip_addr,username=username,password=password,look_for_keys=False,allow_agent=False,port=port)
remote_conn=remote_conn_pre.invoke_shell()

output=remote_conn.recv(5000)
print output

remote_conn.send('show ip int brief\n')
time.sleep(1)
output=remote_conn.recv(5000)
print output
