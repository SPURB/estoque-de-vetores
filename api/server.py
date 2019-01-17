from flask import Flask, jsonify, abort
from flask_cors import CORS
from modules import sections, readdata, endpoints

host = open("host.txt","r").read()
port = 5000
app = Flask(__name__)
cors = CORS(app)
app.config['JSON_AS_ASCII'] = True
base_url = 'http://' + host +':' + str(port) + '/'

@app.route('/')
def home():
	return jsonify({
		'_meta': "home content",
		'content': readdata.read('sections')
	})

@app.route('/valid-sections')
def valid_sections():
	return jsonify({
		'_meta': "valid existing sections",
		'content': sections.names()
	})

@app.route("/endpoints") # http://localhost:5000/section
def get_endpoints():
	return jsonify({
		'_meta': 'list of this app endpoints',
		'endpoints': endpoints.get_all_endpoints(base_url)
	})

@app.route("/<string:name>")
def get_section(name):
		if ( name in sections.names() ):
				return jsonify({
					'_meta': name + "'s" + ' folders content',
					'name': name,
					'content': readdata.read(name)
				})
		else: abort(404)

if __name__ == "__main__":
	app.run(host=host, port=port)
