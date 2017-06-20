print('Create dictionaries')
interface1 = {}
interface1['mtu'] = 1500

interface2 = {'mtu': 1500}

interface3 = dict()
interface3['mtu'] = 1500

print('Are the dictionaries equal?')
print(interface1 == interface2 == interface3)
print('\r\n')

interfaces = [
    {
        'mtu': 1500,
        'speed': 1000,
        'duplex': 'auto',
        'name': 'GigabitEthernet1/0/1'
    },
    {
        'duplex': 'auto',
        'mtu': 1500,
        'name': 'GigabitEthernet1/0/2',
        'speed': 100
    },
    {
        'mtu': 1500,
        'name': 'GigabitEthernet1/0/3',
        'speed': 1000,
        'duplex': 'auto'
    }
]

for interface in interfaces:
    print('='*10, 'Interface', '='*10)
    for key in interface:
        print(key, interface[key])

vlan = {
    11: 'hr',
    12: 'finance',
    31: 'printer',
    21: 'server-internal',
    22: 'server-external',
    23: 'storage'
}

print('All vlans:\t\t\t{}'.format(vlan.keys()))
print('All vlan names:\t\t{}'.format(vlan.values()))
print('All vlan tuples:\t{}'.format(vlan.items()))

v = int(input('VLAN lookup (vlan id): '))
if v in vlan:
    print('Name: {}'.format(vlan[v]))
else:
    print('VLAN id not found')

print('\r\n')
print('for key in vlan:')
for key in vlan:
    print('Vlan {number}: Name: {name}'.format(number=key, name=vlan[key]))

print('for item in vlan.items:')
for item in vlan.items():
    print('Vlan {a}: Name: {b}'.format(a=item[0], b=item[1]))

print('for number, name in vlan.items:')
for number, name in vlan.items():
    print('Vlan {a}: Name: {b}'.format(a=number, b=name))
