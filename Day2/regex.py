import re

x = re.search(r'cat', 'A cat and a rat can\'t be friends.')
print(x)

x = re.search(r'cow', 'A cat and a rat can\'t be friends.')
print(x)

if x:
    print('Match found')

x = re.search(r' .at ', 'A cat and a rat can\'t be friends.')

x = re.search(r'[cr]at ', 'A cat and a rat can\'t be friends.')

t = 'Device1:10.0.0.1,Device2:10.0.0.2'

matches = re.findall(r'(Device\d{1})', t)
for match in matches:
    print(match)

t = 'Device1:10.0.0.1,Device2:10.0.0.2'

matches = re.findall(r'(Device\d{1}):([0-9\.]*)', t)
for match in matches:
    print(match[0])
    print(match[1])


ping = '''Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=48ms TTL=49
Reply from 8.8.8.8: bytes=32 time=52ms TTL=49
Reply from 8.8.8.8: bytes=32 time=51ms TTL=49
Reply from 8.8.8.8: bytes=32 time=44ms TTL=49

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
Minimum = 44ms, Maximum = 52ms, Average = 48ms'''

x = re.search(r'([0-9]*)%',ping)
print('ping match group 0:', x.group(0))
print('ping match group 1:', x.group(1))
if float(x.group(1)) == 0:
    print('ping works')
else:
    print('we have some loss')

stp = '''sw8262-c#show spanning-tree

MST0
  Spanning tree enabled protocol mstp
  Root ID    Priority    8192
             Address     c84c.75fa.6000
             Cost        0
             Port        456 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32768  (priority 32768 sys-id-ext 0)
             Address     0008.2f89.e080
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi0/2               Desg FWD 20000     128.2    P2p Edge
Gi0/3               Desg FWD 20000     128.3    P2p Edge
Gi0/4               Desg FWD 200000    128.4    P2p Edge
Po1                 Root FWD 10000     128.456  P2p'''

x = re.search(r'Root[\s]*ID[\s]*Priority[\s]*([0-9]*)[\s]*Address[\s]*([a-f0-9.]*)', stp)
print('Root priority:', x.group(1))
print('Root address:', x.group(2))
