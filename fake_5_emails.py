from faker import Faker
fake = Faker()

for _ in range(2):
    print("Email: ", fake.email())
    print("Safe Email: ", fake.safe_email())
    print("Free Email: ", fake.free_email())
    print("Company Email: ", fake.company_email())

    print("ASCII Email: ", fake.email())
    print("ASCII Safe Email: ", fake.ascii_safe_email())
    print("ASCII Free Email: ", fake.ascii_free_email())
    print("ASCII Company Email: ", fake.ascii_company_email())