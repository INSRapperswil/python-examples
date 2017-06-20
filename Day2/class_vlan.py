class Vlan(object):
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.dot1q = id
        self.untagged = set()
        self.tagged = set()

    def add_access(self, interface):
        if interface not in self.tagged:
            self.untagged.add(interface)
        else:
            print('ERROR: {} is already a trunk port!'.format(interface))

    def add_trunk(self, interface):
        if interface not in self.untagged:
            self.tagged.add(interface)
        else:
            print('ERROR: {} is already an access port!'.format(interface))

    def ios_config(self):
        interfaces = []
        for interface in self.untagged:
            conf = '  switchport mode access\n  switchport access vlan {id}\n'.format(id=self.dot1q)
            interfaces.append((interface, conf))
        for interface in self.tagged:
            conf = '  switchport mode trunk\n  switchport trunk allowed vlan add {id}\n'.format(id=self.dot1q)
            interfaces.append((interface, conf))
        interfaces.sort()
        result = ''
        for interface, config in interfaces:
            # result += interface + '\n' + config
            result += '\n'.join([interface, config])
        return result


v1 = Vlan(11, 'hr')
v1.add_access('eth7')
v1.add_trunk('eth3')
v1.add_access('eth2')
print(v1.ios_config())


for port in ['1/0/1', '1/3/1', '0/1/1', '0/0/1', '1/2/1', '1/0/45', '1/3/11', '0/4/1', '1/2/3', '1/0/13']:
    v1.add_access('GigabitInterface{}'.format(port))

for port in ['0/0/13', '0/3/1', '0/1/4']:
    v1.add_trunk('GigabitInterface{}'.format(port))

print(v1.ios_config())

v1.add_trunk('eth7')
