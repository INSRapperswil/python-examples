t = '127.0.0.1', 8080, 'tcp'
print(t)
print('allow {2} port {1} on {0}'.format(t[0], t[1], t[2]))
print('allow {2} port {1} on {0}'.format(*t))
print('Count:', t.count(8080))

for i in t:
    print(i)
