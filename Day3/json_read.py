import json

# read multiple objects from file
with open('read_interfaces.json', 'r') as in_file:
    interfaces = json.load(in_file)
    print(interfaces)
    print(type(interfaces))
    for i in interfaces:
        if 'name' in i:
            print('Name: {}'.format(i['name']))
        print(type(i))

# read multiple objects from string
vlan_json = '{"11": "hr", "12": "finance", "31": "printer", "21": "server-internal", "22": "server-external"}'
vlan = json.loads(vlan_json)
print(type(vlan))
for i in vlan.items():
    print('{} --> {}'.format(i[0], i[1]))
