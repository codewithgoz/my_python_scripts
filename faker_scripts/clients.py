# Fake Clients Generator
# Description: Generate a csv file with fake client's data 
# Author: Goz

import csv

from faker import Faker
from faker.providers import job
from faker.providers import date_time

clients_number = input('¿Cuantos clientes necesitas? ')

fake = Faker(['es_ES'])
fake.add_provider(job)
fake.add_provider(date_time)

with open('clients.csv', 'w', newline='') as f:
    file = csv.writer(f)
    for _ in range(int(clients_number)):
        file.writerow([fake.name(), fake.date(), fake.job()])

print("Tus clientes fueron generados!!!")