#! /Users/tahmad/.pyenv/venv/bin/python
# pw.py - An insecure pasword locker program
#   /Users/tahmad/.pyenv/venv/bin/python pw.py blog

PASSWORDS = {'email': 'FDS432SFDSCSfsdfds234',
            'blog': 'VmALcsFSvsfseD32FSFfssd',
            'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]    #first command line arg is the acct name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')
