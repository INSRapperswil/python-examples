import csv

file_out = open('persons.csv', 'w')
columns = ['firstName', 'lastName', 'isAlive', 'age', 'city', 'zipCode']

writer = csv.DictWriter(file_out, fieldnames=columns)
writer.writeheader()
writer.writerow({'firstName': 'Baked',
                 'lastName': 'Beans',
                 'isAlive': True,
                 'age': '25',
                 'city': 'Rapperswil',
                 'zipCode': '8640'})
writer.writerow({'firstName': 'Scrambled',
                 'lastName': 'Eggs',
                 'isAlive': True,
                 'age': '25',
                 'city': 'Rapperswil',
                 'zipCode': '8640'})
file_out.close()



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
file_out = open('interfaces.csv', 'w')
columns = ['name', 'mtu', 'speed', 'duplex']

writer = csv.DictWriter(file_out, fieldnames=columns)
writer.writeheader()
writer.writerows(interfaces)
file_out.close()
