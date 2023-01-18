from faker import Faker
fake = Faker(["en_Au"])

for _ in range(2):
    print("Vehichle License Plate Number: ", fake.license_plate())