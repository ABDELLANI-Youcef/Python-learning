import urllib3
import json
from rich import print_json


# def get_posts():
#   url = "https://jsonplaceholder.typicode.com/posts"
#   try:
#     with urllib3.request.open(url) as response:
#       data = response.read()
#       parsed_data = json.loads(data)
#       return parsed_data
#   except:
#     print(f"[red]Error fetching data: {e}[/red]")
#     return

def get_posts():
  url = "https://jsonplaceholder.typicode.com/posts"
  http = urllib3.PoolManager()
  try:
    response = http.request('GET', url)
    if response.status == 200:
      data = response.data.decode('utf-8')
      parsed_data = json.loads(data)
      return parsed_data
    else:
      print(f"[red]Error fetching data: {response.status}[/red]")
      return []
  except Exception as e:
    print(f"[red]Error fetching data: {e}[/red]")
    return []

def main():
  prosts = get_posts()
  print_json(data=prosts, indent=2)

if __name__ == "__main__":
  main()