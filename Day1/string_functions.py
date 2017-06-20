name = 'Han Solo'

print('upper')
print('-'*3)
print(name.upper())

print('lower')
print('-'*3)

print('username')
print('-'*3)
firstname, surname = name.split(' ')
print('{}.{}'.format(firstname[0].lower(), surname.lower()))

print('=' * 30)
interface = 'GigabitEthernet1/0/1'
print(interface[0:3])
print(interface[:15])
print(interface[-5:])

module, slot, port = interface[-5:].split('/')
print('Module: {0}, Slot: {1}, Port: {2}'.format(module, slot, port))

data = 'Router1:152.96.1.1:vlan230,Router2:152.96.2.1:vlan240,Router3:152.96.3.1:vlan250'

for entry in data.split(','):
    name, ip, vlan = entry.split(':')
    print('Device {0} has ip {1} and is in {2} '.format(name, ip, vlan))

subnetmask = '255.255.255.224'
for octet in subnetmask.split('.'):
    number = int(octet)
    print('int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}'.format(number))

mgmt_ip = 'set interfaces {interface} unit 0 family inet address {address}/{mask}'
print(mgmt_ip.format(interface='me0', address='10.93.15.246', mask='21'))
for i in range(1,10):
    interface = 'me' + str(i)
    address = '10.96.15.' + str(120 + i)
    cidr = '21'
    print(mgmt_ip.format(interface=interface, address=address, mask=cidr))
