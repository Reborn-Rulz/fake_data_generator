from faker import Faker
fake = Faker(["en_AU"])

print("Bank ABA Transit Number: ", fake.aba())
print("Bank Country: ", fake.bank_country())
print("Basic Bank Account Number: ", fake.bban())
print("International Bank Account Number: ", fake.iban())
print("Swift Bank Account Number: ", fake.swift(length=11))