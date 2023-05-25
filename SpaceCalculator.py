

# Calculates the amount of people in space, and lists their names and respective spacecrafts
import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print("There are a total of " + str(json['number']) + " people in space. Their names are:")
for person in json['people']:
    print(person['name'] + " of the spacecraft " + person['craft'])
