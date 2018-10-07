from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World guys from BC!'

@app.route('/by')
def by():
	return 'It''s me!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')

