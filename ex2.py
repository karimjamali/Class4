import paramiko
from getpass import getpass
import time
import sys

class Remote_Connect(object):
  def __init__ (self,ip_addr,username,password,port):
    self.ip_addr=ip_addr
    self.username=username
    self.password=password
    self.port=port
    
  def SSH_Connection(self):
    remote_conn_pre=paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()
    try:
      remote_conn_pre.connect(self.ip_addr,username=self.username,password=self.password,look_for_keys=False,allow_agent=False,port=self.port)
      return remote_conn_pre
    except paramiko.ssh_exception.AuthenticationException:
      sys.exit('Authentication failed')
  def disable_paging(self,remote_conn):
    remote_conn.send('terminal length 0 \n')
  def invoke_shell(self,remote_conn_pre):
   remote_conn=remote_conn_pre.invoke_shell()
   return remote_conn
  def save_output_to_file(self,output,a_file):
    with open(a_file,'a') as f:
      f.write(output)
  def send_command(self,remote_conn,cmd):
    output1=''
    remote_conn.send(cmd + '\n')
    time.sleep(1)
    while remote_conn.recv_ready():
     output1+=remote_conn.recv(5000)
    return output1
def main():
   ip_addr='50.76.53.27'
   username='pyclass'
   password=getpass()
   port = 8022

   SSH=Remote_Connect(ip_addr,username,password,port)
   remote_conn_pre=SSH.SSH_Connection()
   remote_conn=SSH.invoke_shell(remote_conn_pre)
   SSH.disable_paging(remote_conn)
   output=SSH.send_command(remote_conn,'show run | inc logging')
   print output
   output=SSH.send_command(remote_conn,'configure terminal')
   SSH.send_command(remote_conn,'logging buffered 64555')
   output=SSH.send_command(remote_conn,'do show run | inc logging')
   print output
   SSH.save_output_to_file(output,'logging-buffered.txt')


if __name__ =='__main__':
   main()

