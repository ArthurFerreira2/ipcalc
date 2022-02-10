
Exploring the ipaddress python module with an interactive ipv4 / ipv6 calc  
This is a work in progress - actually unusable as is

```
$ ./ipcalc.py
> help

    na host/mask   returns the network address of the host
    bd host/mask   returns the broadcast address of the host
    hs net/mask    returns the the hosts of the network
    nm net/mask    returns the netmask of the network
    hm net/mask    returns the hostmask of the network
    E6 v6addr      returns the exploded IPv6 adddress
    C6 v6addr      returns the compressed IPv6 address
    RP addr        returns the reverse pointer

> na 192.168.1.23
192.168.1.23/32
> bd 192.168.1.23/23
192.168.1.255
> nm 192.168.0.0/23
255.255.254.0
> hm 192.168.0.0/23
0.0.1.255
> hs 192.168.1.16/29
192.168.1.17
192.168.1.18
192.168.1.19
192.168.1.20
192.168.1.21
192.168.1.22
> e6 2001:db8::1
2001:0db8:0000:0000:0000:0000:0000:0001
> c6 2001:0db8:0000:0000:0000:0000:0000:0001
2001:db8::1
> rp 192.168.1.20
20.1.168.192.in-addr.arpa
> rp 2001:db8::1
1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa
>
```
