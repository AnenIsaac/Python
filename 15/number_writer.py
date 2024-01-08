import json

numbers = [1, 2, 5, 7, 12, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)