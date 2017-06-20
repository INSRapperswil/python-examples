import json

person = {
    'firstName': 'John',
    'lastName': 'Smith',
    'isAlive': True,
    'age': 25,
    'city': 'Rapperswil',
    'zipCode': '8640'
}

out_file = open('person.json', 'w')
json.dump(person, out_file)
out_file.close()

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

out_file = open('interfaces.json', 'w')
json.dump(interfaces, out_file)
out_file.close()

vlan = {
    11: 'hr',
    12: 'finance',
    31: 'printer',
    21: 'server-internal',
    22: 'server-external',
    23: 'storage'
}

vlan_json = json.dumps(vlan)
print(vlan_json)
print(type(vlan_json))
