print('open file')
filename = 'textfile.txt'
file_input = open(filename)
print('read separator')
print('remove spaces or newline with .strip()')
separator = file_input.readline().strip()
print('separator:', separator)

print('read number of lines')
line_number = int(file_input.readline())
print('number of lines:', line_number)

svi = []
vlan = []
for i in range(line_number):
    line = file_input.readline().strip()
    parameters = line.split(sep=separator)
    vlan.append('vlan {nr}\n  name {n}'.format(nr=parameters[0], n=parameters[1]))
    svi.append('interface vlan {nr}\n'
               '  description {name}\n'
               '  ip address {ip} {mask}\n'
               '  no shutdown'.format(nr=parameters[0], name=parameters[1], ip=parameters[2], mask=parameters[3]))

file_input.close()
print(vlan)
print(svi)

for i in vlan:
    print(i)

for i in svi:
    print(i)

print('=' * 30)
print('write file')
filename = 'configuration.cfg'
file_output = open(filename, 'w')
for i in vlan:
    file_output.write(i)
    file_output.write('\n')
for i in svi:
    file_output.write(i)
    file_output.write('\n')

file_output.close()

file_input = open(filename)
config = file_input.read()
print(config)