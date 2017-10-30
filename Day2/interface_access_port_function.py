my_interfaces = ['Gig0/1', 'Gig0/2', 'Gig0/3', 'Gig0/4']
my_vlans = [100, 200, 300, 100]


def generate_access_port(interfaces, vlans):
    for position in range(len(interfaces)):
        interface = interfaces[position]
        vlan = vlans[position]
        print('interface {0}'.format(interface))
        print('  description python')
        print('  switchport acceess vlan {0}'.format(vlan))
        print()

generate_access_port(my_interfaces, my_vlans)

my_interfaces2 = ['Gig0/11', 'Gig0/12', 'Gig0/13', 'Gig0/14']
my_vlans2 = [10, 120, 30, 11]

generate_access_port(my_interfaces2, my_vlans2)