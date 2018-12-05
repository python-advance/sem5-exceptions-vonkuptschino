import json
from tabulate import tabulate
import re

try:
    f = open("strings.json", 'rb')
except IOError:
    print("Could not read file: strings.json")
    sys.exit()

with open("strings.json") as json_data:
    d = json.load(json_data)
    #print(type(d))
with open("newRaw.txt", 'w') as file:
    file.write(tabulate(d))
    file.close()

try:
    f = open("newRaw.txt", 'rb')
except IOError:
    print("Could not read file: newRaw.txt")
    sys.exit()

with open("newRaw.txt") as open_file:
    data = open_file.read()

with open("newTable.txt", 'w') as file:
    file.write(re.sub('[{}:,\']', '', data))

if __name__ == '__main__':
	assert(type(data) == type('string'), "data is not a string!")
