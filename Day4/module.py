import lib.data_import
from lib.printer import header, error, repeat

vlan_json = '{"11": "hr", "12": "finance", "31": "printer", "21": "server-internal", "22": "server-external"}'
test = lib.data_import.jsonstring2dict(vlan_json)
print(test)
print(test.keys())
repeat('\n', 3)
repeat('echo', 2)
header('Title')
error('to many DJs')
