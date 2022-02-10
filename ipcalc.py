#!/usr/bin/env python3

# Copyright (c) 2022 Arthur Ferreira
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# exploring the ipaddress module
# https://docs.python.org/3.7/library/ipaddress.html

import ipaddress

while True:

  print ('>', end=' ')
  command = input().split(' ')

  if command[0].upper() == 'QUIT' or command[0].upper() == 'Q':
    print('bye')
    exit(0)

  if command[0].upper() == 'HELP' or command[0].upper() == 'H':
    print("""
    na host/mask   returns the network address of the host
    bd host/mask   returns the broadcast address of the host
    nm net/mask    returns the netmask of the network
    hm net/mask    returns the hostmask of the network
    hs net/mask    returns all the hosts of the network
    E6 v6addr      returns the exploded IPv6 adddress
    C6 v6addr      returns the compressed IPv6 address
    RP addr        returns the reverse pointer
    """)
    continue

  if command[0].upper() == 'NA':
    try:
      addr = ipaddress.ip_interface(''.join(command[1:]))
      print(addr.network)
    except ValueError:
      print('%s is not a valid address' % command[1])
    continue

  if command[0].upper() == 'BD':
    try:
      addr = ipaddress.ip_interface(''.join(command[1:]))
      print(addr.network[-1])
    except ValueError:
      print('%s is not a valid address' % command[1])
    continue

  if command[0].upper() == 'HS':
    try:
      net = ipaddress.ip_network(''.join(command[1:]))
    except ValueError:
      print('%s is not a valid network' % command[1])
      continue
    for host in net.hosts():
      print(host)
    continue

  if command[0].upper() == 'NM':
    try:
      addr = ipaddress.ip_network(''.join(command[1:]))
      print(addr.netmask)
    except ValueError:
      print('%s is not a valid network' % command[1])
    continue

  if command[0].upper() == 'HM':
    try:
      addr = ipaddress.ip_network(''.join(command[1:]))
      print(addr.hostmask)
    except ValueError:
      print('%s is not a valid network' % command[1])
    continue

  if command[0].upper() == 'E6':
    try:
      addr = ipaddress.IPv6Address(''.join(command[1:]))
      print(addr.exploded)
    except ValueError:
      print('%s is not a valid ipv6 host address' % command[1])
    continue

  if command[0].upper() == 'C6':
    try:
      addr = ipaddress.IPv6Address(''.join(command[1:]))
      print(addr.compressed)
    except ValueError:
      print('%s is not a valid ipv6 host address' % command[1])
    continue



  if command[0].upper() == 'RP':
    try:
      addr = ipaddress.ip_address(''.join(command[1:]))
      print(addr.reverse_pointer)
    except ValueError:
      print('%s is not a valid host address' % command[1])
    continue

  else:
    print('Unknown command %s' % ' '.join(command))
