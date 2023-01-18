from faker import Faker
fake = Faker(["en_AU"])

print("Job Post: ", fake.job())
print("Company Name: ", fake.company())
print("Company Slogen: ", fake.bs())
print("Company Phrase: ", fake.catch_phrase())
print("Company Suffix: ", fake.company_suffix())