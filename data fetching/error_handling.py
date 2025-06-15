from rich import print_json
import requests

def get_something_error():
  url = "https://jsonplaceholder.typicode.com/xyz"
  try:
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()
    return response_json
  except  requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
  except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    return

def main():
  response = get_something_error()
  print_json(data=response, indent=2)
  return

if __name__ == "__main__":
  main()