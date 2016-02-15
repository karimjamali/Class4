#!/usr/bin/env python
import pexpect
from getpass import getpass
import re

def main():
  ip_addr='50.76.53.27'
  username='pyclass'
  port=8022
  password=getpass()
  
  ssh_conn=pexpect.spawn('ssh -l {} {} -p {}' .format(username,ip_addr,port))
  ssh_conn.timeout=3
  #ssh_conn.sendline('yes')
  ssh_conn.expect('ssword:')
  ssh_conn.sendline(password)
  ssh_conn.expect('#')
  #print ssh_conn.before
  ssh_conn.sendline('terminal length 0')
  ssh_conn.expect('#')
  #ssh_conn.sendline('show version')
  #ssh_conn.expect('pynet-rtr2#') 
 # print ssh_conn.before

  #pattern=re.compile(r'^Lic.*DI:.*$',re.MULTILINE)
  #ssh_conn.sendline('show version') 
  #ssh_conn.expect('pynet-rtr2#')
  #print ssh_conn.before
  ssh_conn.sendline('configure terminal')
  ssh_conn.expect('#')
  ssh_conn.sendline('do show run | inc logging')
  ssh_conn.expect('#')
  print ssh_conn.before
  ssh_conn.sendline('logging buffered 64125')
  ssh_conn.sendline('do show run | inc logging')
  ssh_conn.expect('#')
  print ssh_conn.before
  
  #print ssh_conn.before 
 # try:
  #  ssh_conn.sendline('show version')
   # ssh_conn.expect('zzzzzzzzz')
 # except pexpect.TIMEOUT:
  #  print "Found Timeout"

if __name__ == "__main__":
     main()

  
