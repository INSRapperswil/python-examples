vlans = [11, 12, 13, 14, 15, 21, 22]
print(vlans)
print('Add vlan 16')
vlans.append(16)
print(vlans)
print('Sort the item of the list')
vlans.sort()
print(vlans)
print('Add 11 again')
vlans.append(11)
print(vlans)
print('How many 11 are in the list?')
print(vlans.count(11))
print('Delete fist 11')
vlans.remove(11)
print(vlans)
print('First 4 items')
print(vlans[0:4])
print('Last 4 items')
print(vlans[-4:])
print('Remove and print the last item')
print(vlans.pop())
print('\n')

print('Create a range list from 100 to 4095\n'
      '  - reverse the elements\n'
      '  - create 10 vlans and use your created pool')
vlan_pool = list(range(100, 4095))
vlan_pool.reverse()
for i in range(10):
    print('Create Vlan {}'.format(vlan_pool.pop()))

print('Divisible by x and y list')
x = int(input('x: '))
y = int(input('y: '))
start = int(input('Range start: '))
end = int(input('Range end (inclusive): '))+1
divisible_by = []
for i in range(start, end):
    if i % x == 0 and i % y == 0:
        divisible_by.append(i)

print(divisible_by)
print('Length: {}'.format(len(divisible_by)))

print('inefficient way to find prime numbers')
stop = int(input('Stop: '))
primes = []
for n in range(1, stop):
    count = 0
    for m in range(2, int(n/2)):
        if n % m == 0:
            count += 1
    if count == 0:
        primes.append(n)

print(primes)
print(len(primes))
