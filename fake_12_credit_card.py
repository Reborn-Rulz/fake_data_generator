from faker import Faker
fake = Faker()

print("Credit Card Expiry Date: ", fake.credit_card_expire())
print("Credit Card Details: ", fake.credit_card_full())
print("Credit Card Provider: ", fake.credit_card_provider())
print("Credit Card Number ", fake.credit_card_number(card_type="maestro"))
print("Credit Card CVC: ", fake.credit_card_security_code())