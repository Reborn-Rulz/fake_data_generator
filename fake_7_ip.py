from faker import Faker
fake = Faker() # ["en_AU"]

print("IPV4: ", fake.ipv4())
print("IPV6: ", fake.ipv6())
print("IPV4 Private: ", fake.ipv4_private())
# print("IPV6 Private: ", fake.ipv6_private())
print("IPV4 Public: ", fake.ipv4_public())
# print("IPV6 Public: ", fake.ipv6_public())
print("Port Number: ", fake.port_number())
print("MAC Address: ", fake.mac_address())