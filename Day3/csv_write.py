import csv

# write multiple rows one by one to file
with open('persons.csv', 'w') as file_out:
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

# write multiple rows at once to file
interfaces = [
    {
        'mtu': 1500,
        'speed': 1000,
        'duplex': 'auto',
        'name': 'GigabitEthernet1/0/1'
    },
    {
        'mtu': 1500,
        'speed': 100,
        'duplex': 'auto',
        'name': 'GigabitEthernet1/0/2'
    },
    {
        'mtu': 1500,
        'speed': 1000,
        'duplex': 'auto',
        'name': 'GigabitEthernet1/0/3'
    }
]

with open('interfaces.csv', 'w') as file_out:
    columns = ['name', 'mtu', 'speed', 'duplex']

    writer = csv.DictWriter(file_out, fieldnames=columns)
    writer.writeheader()
    writer.writerows(interfaces)
