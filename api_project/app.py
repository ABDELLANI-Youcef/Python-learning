from bottle import route, run, response

@route('/')
def home():
  return "Welcome to the API Project!"

@route('/hello/<name>')
def hello(name):
  return f"Hello, {name}! youcef are amazing!"

if __name__ == "__main__":
  run(host='localhost', port=8080, debug=True, reloader=True)