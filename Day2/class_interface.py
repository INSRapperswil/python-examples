class Interface:
    def __init__(self, interface_name):
        self.name = interface_name
        self.disabled = True
        self.connected = False
        self.up = False

    def _check_status(self):
        if self.connected and not self.disabled:
            if not self.up:
                self.up = True
                print('Interface {} changed to up'.format(self.name))
                return
        if self.up:
            self.up = False
            print('Interface {} changed to down'.format(self.name))

    def enable(self):
        if self.disabled:
            print('Enable interface {}'.format(self.name))
            self.disabled = False
        self._check_status()

    def disable(self):
        if not self.disabled:
            print('Disable interface {}'.format(self.name))
            self.disabled = True
        self._check_status()

    def add_cable(self):
        if self.connected:
            print('Interface {} already patched'.format(self.name))
            return
        self.connected = True
        self._check_status()

    def remove_cable(self):
        if not self.connected:
            print('Interface {} is not patched'.format(self.name))
            return
        self.connected = False
        self._check_status()

    def status(self):
        return self.up

gig1 = Interface('GigabitInterface1/0/1')
gig1.enable()
gig1.add_cable()

if gig1.status():
    print('Interface is up')
    gig1.disable()
    gig1.enable()
print('remove cable')
gig1.remove_cable()
print('remove cable again')
gig1.remove_cable()
print('add cable')
gig1.add_cable()
