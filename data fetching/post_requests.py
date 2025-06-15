import requests
from rich import print_json

def get_posts(url, post_body):
  response = requests.post(url, post_body)

  parsed_json = response.json()
  return parsed_json

def main():
  new_post = {
    "userId": 4,
    "title": "Sample Post",
    "body": "This is a sample post for testing purposes."
  }
  url = "https://jsonplaceholder.typicode.com/posts"
  posts = get_posts(url, new_post)
  print_json(data=posts, indent=2)

if __name__ == "__main__":
  main()