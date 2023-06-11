import os
import pexpect
from getpass import getpass

password = getpass('Enter IST password: ')

# Copy .sql files
for filename in os.listdir('.'):
    if filename.endswith('.sql'):
        print("sending", filename)
        child = pexpect.spawn(f'scp {filename} ist1102666@sigma.tecnico.ulisboa.pt:')
        child.expect('ist1102666@sigma.tecnico.ulisboa.pt\'s password:')
        child.sendline(password)
        child.expect(pexpect.EOF)

# Copy .py and .cgi files in the web folder
web_directory = '/afs/.ist.utl.pt/users/6/6/ist1102666/web' 
for filename in os.listdir('web'):
    if filename.endswith(('.py', '.cgi')):
        print("sending", filename)
        child = pexpect.spawn(f'scp web/{filename} ist1102666@sigma.tecnico.ulisboa.pt:{web_directory}')
        child.expect('ist1102666@sigma.tecnico.ulisboa.pt\'s password:')
        child.sendline(password)
        child.expect(pexpect.EOF)

print('Files copied successfully')





