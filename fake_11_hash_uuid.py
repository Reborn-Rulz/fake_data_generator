from faker import Faker
fake = Faker()

print("Fake md5: ", fake.md5())
print("Fake sha1: ", fake.sha1())
print("Fake sha2565: ", fake.sha256())
print("Fake uuid4: ", fake.uuid4())