import csv

file_in = open('read_interfaces.csv', 'r')

reader = csv.DictReader(file_in)
for row in reader:
    print('{0} \t{1} \t{2} \t{3}'.format(row['name'], row['mtu'], row['speed'], row['duplex']))

file_in.close()
