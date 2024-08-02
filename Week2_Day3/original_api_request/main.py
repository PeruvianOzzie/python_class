import requests

print(requests)

API_URL_POSTS = "https://jsonplaceholder.typicode.com/posts?_limit=20"

response = requests.get(API_URL_POSTS).json()

for post in response:
    print(f"- {post}")