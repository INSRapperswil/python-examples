import napalm_base

driver = napalm_base.get_network_driver('ios')
device = driver(hostname='R11.lab.local', username='ins', password='ins')
device.open()
facts = device.get_facts()
device.close()
for key, value in facts.items():
    print('{:20}{}'.format(key, value))
