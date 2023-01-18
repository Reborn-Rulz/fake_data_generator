from faker import Faker

fake = Faker() #["en_CA"]

print("Full Name: ", fake.name())
print("First Name: ", fake.first_name())
print("Last Name: ", fake.last_name())
print("First Name Female: ", fake.first_name_female())
print("Last Name Male: ", fake.last_name_male())
print("Full Name Female: ", fake.name_female())
print("Full Name Male: ", fake.name_male())
print("Prefix Name: ", fake.prefix())
print("Suffix Name: ", fake.suffix())