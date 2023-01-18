from faker import Faker
fake = Faker(["en_AU"])

print("Currency: ", fake.currency())
print("Currency Name: ", fake.currency_name())
print("Currency Code: ", fake.currency_code())
print("Cryptcurrency Name: ", fake.cryptocurrency_name())