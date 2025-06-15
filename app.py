from bottle import route, run, response, template

countries = [
  {"name": "Algeria", "capital": "Algiers", "population": 43851044},
  {"name": "Egypt", "capital": "Cairo", "population": 104124440},
  {"name": "Morocco", "capital": "Rabat", "population": 36910560},
  {"name": "Tunisia", "capital": "Tunis", "population": 11818619},
  {"name": "Libya", "capital": "Tripoli", "population": 6871292}
]

@route('/')
def home():
  return template('home', countries=countries)

@route('/hello/<name>')
def hello(name):
  return f"Hello, {name}! youcef are amazing!"

@route('/countries')
def get_countries():
  response.content_type = 'application/json'
  return {"countries": countries}

if __name__ == "__main__":
  run(host='localhost', port=8080, debug=True, reloader=True)