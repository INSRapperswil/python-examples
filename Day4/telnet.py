import getpass
import telnetlib

host = input('Host: ')
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)
tn.read_until(b"login: ", timeout=1)
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ", timeout=1)
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"show version\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))