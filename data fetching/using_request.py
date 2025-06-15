import requests
from rich import print_json

def get_posts(url):
  response = requests.get(url)

  parsed_json = response.json()
  return parsed_json

def main():
  url = "https://jsonplaceholder.typicode.com/posts"
  posts = get_posts(url)
  print_json(data=posts, indent=2)

if __name__ == "__main__":
  main()