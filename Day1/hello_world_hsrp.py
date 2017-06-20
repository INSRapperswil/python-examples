vlan = 100
local_ip = 2

print('''interface Vlan{0}
  description HelloWorld
  ip address 152.96.{0}.{1}/24
  ipv6 address 2001:620:130:{0}::{1}/64
  hsrp version 2
  hsrp {0}
    authentication md5 key-chain hsrp-key
    preempt
    priority 110
    ip 152.96.{0}.1
  hsrp {0} ipv6
    authentication md5 key-chain hsrp-key
    preempt
    priority 110
    ip 2001:620:130:{0}::1'''.format(vlan, local_ip))
