import json

with open('salaries.json') as jf:
    salaries = json.loads(jf.read())

for year in salaries:
    fee = salaries[year]["fee"]
    fee_dollar = salaries[year]["fee"] / salaries[year]["dollar_rate"]
    print(f'{year}: {fee} руб., ${fee_dollar}')
