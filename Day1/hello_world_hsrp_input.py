print('Create HSRP config')

vlan = input('Vlan: ')
local_ip = input('Local IP: ')

print('HSRP Config\tVlan: {vlan}\tIP: {ip}'.format(vlan=vlan, ip=local_ip))
print('-----')

print('''interface Vlan{vlan}
  description HelloWorld
  ip address 152.96.{vlan}.{ip}/24
  ipv6 address 2001:620:130:{vlan}::{ip}/64
  hsrp version 2
  hsrp {vlan}
    authentication md5 key-chain hsrp-key
    preempt
    priority 110
    ip 152.96.{vlan}.1
  hsrp {vlan} ipv6
    authentication md5 key-chain hsrp-key
    preempt
    priority 110
    ip 2001:620:130:{vlan}::1'''.format(vlan=vlan, ip=local_ip))
