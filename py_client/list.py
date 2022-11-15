import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'
username = input('What is your username?\n')
password = getpass('What is your password?\n')

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
  token = auth_response.json()['token']
  headers = {
    'Authorization': f'Bearer {token}'
  }
  endpoint = 'http://localhost:8000/api/products/'

  get_response = requests.get(endpoint, headers=headers)
  print(get_response.json())
  data = get_response.json()
  next_url = data['next']
  results = data['results']

  print('\n\n\n')

  count = 1
  while next_url is not None:
    get_response = requests.get(next_url, headers=headers)
    data = get_response.json()
    next_url = data['next']
    count += 1
    print(count)
    print(get_response.json())
