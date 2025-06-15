import requests
from rich import print_json

def get_posts(url, user_id = 7):
  user_params = {'userId': user_id}
  response = requests.get(url, user_params)

  parsed_json = response.json()
  return parsed_json

def main():
  url = "https://jsonplaceholder.typicode.com/posts"
  posts = get_posts(url, 4)
  print_json(data=posts, indent=2)

if __name__ == "__main__":
  main()