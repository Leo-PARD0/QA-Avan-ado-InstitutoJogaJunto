from faker import Faker
 
fake = Faker("pt-BR")
print ("Nome: ", fake.name())
print ("Email: ", fake.email())
print ("Cidade: ", fake.city())
print ('idade: ', fake.random_int(min=0, max=120)) # o métoedo random_int precisa de um mínimo e/ou máximo, se não gera valores aléatorios sem critério. Para idade, 4623 anos é um absurdo.
