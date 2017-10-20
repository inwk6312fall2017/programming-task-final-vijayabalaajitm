
import select
import paramiko
import re
fd = open(r'C:\NewdayTest.txt','w') 
old_stdout = sys.stdout   
sys.stdout = fd 
platform = 'cisco_ios'
username = 'username' 
password = 'password' 

ip_add_file = open(r'C:\IPAddressList.txt','r') you want to connect to each one on a new line

for host in ip_add_file:
    host = host.strip()
    fd.close()
