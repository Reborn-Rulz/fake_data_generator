from faker import Faker
fake = Faker(["en_AU"])

for _ in range(2):
    print("Phone Number: ", fake.phone_number())
    print("Country Calling Code: ", fake.country_calling_code())
    print("MSISDN: ", fake.msisdn())