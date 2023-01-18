from faker import Faker
fake = Faker(["en_AU"])

# for _ in range(2):
print("User Name: ", fake.user_name())
print("Hostname: ", fake.hostname())
print("Domain Name: ", fake.domain_name())
print("Domain Word: ", fake.domain_word())
print("TLD: ", fake.tld())

print("URL: ", fake.url())
print("URI: ", fake.uri())
print("URI Extension: ", fake.uri_extension())
print("URI Path: ", fake.uri_path())
print("Slug: ", fake.slug())
print("Image URL: ", fake.image_url())
print("Request Method: ", fake.http_method())