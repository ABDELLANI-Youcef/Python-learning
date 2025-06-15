from bottle import route, run

@route('/')
def home():
  return "Welcome to the API Project!"

if __name__ == "__main__":
  run(host='localhost', port=8080, debug=True, reloader=True)