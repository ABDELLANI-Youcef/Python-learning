from urllib import request
import json
from rich import print_json


def get_posts():
  url = "https://jsonplaceholder.typicode.com/posts"
  try:
    response = request.urlopen(url)
    data = response.read()
    posts = json.loads(data)
    return posts

  except Exception as e:
    print(f"Error decoding JSON: {e}")
    return []

def main():
  prosts = get_posts()
  print_json(data=prosts, indent=2)

if __name__ == "__main__":
  main()