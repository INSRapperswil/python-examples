set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

print('sets are sorted')
print(set1, '\t\t', set2)
set1.add(5)
set2.add(4)
print(set1, '\t', set2)
for i in range(4):
    print('add 5 to set1')
    set1.add(5)
print(set1)

print('\n')
switch1_vlans = [1, 11, 13, 14, 15, 16, 18, 21, 22, 23, 24, 31, 32, 33, 34]
switch2_vlans = [1, 11, 12, 14, 15, 16, 17, 18, 22, 23, 24, 25, 31, 32, 34]
print('Vlans on Switch01:', switch1_vlans)
print('Vlans on Switch02:', switch2_vlans)

switch1_vlans_set = set(switch1_vlans)
switch2_vlans_set = set(switch2_vlans)

print('Are vlan 11 and 12 in both sets?')
print('Switch01:', {11, 12}.issubset(switch1_vlans_set))
print('Switch02:', {11, 12}.issubset(switch2_vlans_set))

print('union')
print(switch1_vlans_set.union(switch2_vlans_set))

print('intersection')
print(switch1_vlans_set.intersection(switch2_vlans_set))

print('difference Switch01 Switch02')
print(switch1_vlans_set.difference(switch2_vlans_set))

print('difference Switch02 Switch01')
print(switch2_vlans_set.difference(switch1_vlans_set))

print('symmetric difference')
print(switch1_vlans_set.symmetric_difference(switch2_vlans_set))
