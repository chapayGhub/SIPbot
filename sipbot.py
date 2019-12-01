#!/usr/bin/python3
import os, sys, signal, subprocess, urllib.request

signal.signal(signal.SIGHUP, signal.SIG_IGN)

number = ""
caller = sys.stdin.readline().strip()

try:
    number = caller[5:] # sipbot will send: 'CALL 0123456\n'
except Exception as e:
    sys.stderr.write('Invalid caller ID: ' + caller + '\n')
    sys.stdout.write('KILL\n')
    sys.exit(1)


allowed = False

with open('authorised.txt') as f:
    for line in f:
        if number == line.strip():
            allowed = True

sys.stderr.write(number + (' called\n' if allowed else ' *** REJECTED ***\n'))

if not allowed:
    sys.stdout.write('KILL\n')
    sys.exit(2)

with urllib.request.urlopen(os.environ["ACTION_CALL"]) as response:
  response.read()

close = False

try:
    line = sys.stdin.readline()
    while line:
        event = line.strip()
        if event == 'DISC':
            close = True
            break
        elif event == 'DTMF *':
            sys.stdout.write('KILL\n')
            break
        else:
            line = sys.stdin.readline()
except e:
    sys.stderr.write(number + ' call error: ' + e.message + '\n')

if close:
    sys.stderr.write(number + ' hung up\n')
    with urllib.request.urlopen(os.environ["ACTION_HANGUP"]) as response:
        response.read()
else:
    sys.stderr.write(number + ' disconnected\n')

