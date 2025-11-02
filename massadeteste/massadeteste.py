from faker import Faker
 
fake = Faker("pt-BR")
print ("Nome:", fake.name())
print ("Email:", fake.email())
print ("Cidade:", fake.city())
