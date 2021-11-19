import requests, json

FOLDER = '/Users/aniron/Documents/BofA_Python_Training_15Nov21/day3/data/'
response = requests.get("https://jsonplaceholder.typicode.com/todos", verify=False)

todos = json.loads(response.text)
# print(todos) ### simple string

### Memory level serialization
data = json.dumps(todos, indent=2) ### "dumps" to memory
print(data) ### This is json now, with good indentation

### File level serialization
with open(FOLDER+'datafile.json', 'w') as writer:
    json.dump(data, writer) ### "dump" to a file
    print('Json data serialized')

# Deserialize the file
with open(FOLDER+'datafile.json', 'r') as reader:
    data = json.load(reader)
    print(data)
