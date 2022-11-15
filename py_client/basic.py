import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": 'Hello world'}) # HTTP REQUEST
# print(get_response.text) # print raw text response

print(get_response.status_code) # print status code

print(get_response.json()) # print json response
