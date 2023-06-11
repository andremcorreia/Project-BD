import os
import pexpect
from getpass import getpass

password = getpass('Enter IST password: ')

for filename in os.listdir('.'):
    if filename.endswith('.sql'):# or filename.endswith('.py'):
        print("sending", filename)
        child = pexpect.spawn(f'scp {filename} ist1102666@sigma.tecnico.ulisboa.pt:')
        child.expect('ist1102666@sigma.tecnico.ulisboa.pt\'s password:')
        child.sendline(password)
        child.expect(pexpect.EOF)

print('Files copied successfully')




