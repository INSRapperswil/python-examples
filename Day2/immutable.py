print('=' * 3, 'Immutable', '=' * 3)
print('Strings are immutable')
interface = 'GigabitEthernet1/0/1'
print(interface.upper())
print('Variable is still lower und upper case')
print(interface)

vlan = 'vlan'
print(vlan)
print('Internal id for vlan variable: {} '.format(id(vlan)))
vlan += '11'
print(vlan)
print('Internal id for vlan variable has changed: {} \t<--- new object created'.format(id(vlan)))

print('\n')
print('=' * 3, 'Mutable', '=' * 3)
vlan_list = [1, 2, 10, 15]
print(vlan_list)
print('Internal id for vlan_list variable: {}'.format(id(vlan_list)))
vlan_list.append(20)
print(vlan_list)
print('Internal id for vlan_list variable is unchanged: {} '.format(id(vlan)))
