import napalm_base
from jinja2 import Template

config_template = '''{% for svi in data -%}
interface GigabitEthernet1.{{ svi.vlan }}
 description {{ svi.description|default('SVI') }}
 encapsulation dot1Q {{ svi.vlan }}
 ip address {{ svi.ip }} {{ svi.mask|default('255.255.255.0') }}
 ip pim dense-mode
!
{% endfor -%}
'''

svi_data = [
    {
        'vlan': 11,
        'description': 'Test svi',
        'ip': '192.168.11.1',
        'mask': '255.255.255.0'
    },
    {
        'vlan': 12,
        'ip': '192.168.12.1'
    },
    {
        'vlan': 13,
        'ip': '192.168.13.1',
        'description': 'server-internal'
    }
]

template = Template(config_template)
config = template.render(data=svi_data)
print('Rendered template:')
print(config)

driver = napalm_base.get_network_driver('ios')
device = driver(hostname='R11.lab.local', username='ins', password='ins')
device.open()

device.load_merge_candidate(config=config)

print('Config difference:')
print(device.compare_config())

device.commit_config()
device.close()

print('Device configured with NAPALM')